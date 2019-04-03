from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource, LabelSet
from bokeh.models.formatters import DatetimeTickFormatter
from bokeh.embed import components
from bokeh.transform import cumsum
import pandas as pd
from math import pi
import matplotlib.pyplot as plt

default_sizing = 'scale_width'


def graph_power_lifting_relative_personal_best(scores, averages, index):
    data = {'athlete': scores, 'average': averages}
    df = pd.DataFrame(data, index=index)

    # Number of variables
    categories = df.index
    N = len(df.index)

    # We are going to plot the first column of the data frame
    # But we need to repeat the first value to close the circular graph
    athlete_values = df['athlete'].values.flatten().tolist()
    athlete_values += athlete_values[:1]

    average_values = df['average'].values.flatten().tolist()
    average_values += average_values[:1]

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    fig = plt.figure(figsize=(10, 10))
    ax = plt.subplot(111, polar=True)

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable
    plt.xticks(angles[:-1], categories, color='grey', size=6)

    # Draw y labels
    ax.set_rlabel_position(0)

    # Find maximum y-value
    max_score = int(max(max(scores, averages)))

    y_values = []
    y_labels = []
    for i in range(0, max_score + 10, 10):
        y_values.append(i)
        y_labels.append(str(i))

    plt.yticks(y_values, y_labels, color="grey", size=6)
    plt.ylim(0, max_score + 10)

    # Plot data
    ax.plot(angles, athlete_values, linewidth=1, linestyle='solid', label='Athlete')
    ax.plot(angles, average_values, linewidth=1, linestyle='solid', label='Division Average')

    # Fill area
    ax.fill(angles, athlete_values, 'b', alpha=0.1)
    ax.fill(angles, average_values, 'r', alpha=0.1)

    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

    plt.savefig('../static/img/athlete_power_lifting_relative_personal_best.png')


def graph_athlete_progress(dates, scores):
    x_axis_label = 'Date'
    y_axis_label = 'Score'

    graph = figure(x_axis_label=x_axis_label, x_axis_type='datetime',
                   y_axis_label=y_axis_label)

    # Automatically adjust graph size
    graph.sizing_mode = default_sizing

    # Format axes
    graph.xaxis.formatter = DatetimeTickFormatter(days='%F', months='%F', years='%F')

    # Show data points on hover
    graph.add_tools(HoverTool(tooltips=[('x,y', '@x{%F}, @y')], formatters={'x': 'datetime'}, mode='mouse'))

    # Plot athlete line
    graph.line(dates, scores, line_color="#5466E2", line_width=2)
    graph.circle(dates, scores, size=10, color="#5466E2")

    # Remove toolbar from graph
    graph.toolbar_location = None

    return components(graph)


def graph_compare_divisions(divisions, div_ave_scores):
    x_axis_label = 'Divisions'
    y_axis_label = 'Average Scores'

    graph = figure(x_axis_label=x_axis_label, y_axis_label=y_axis_label, x_range=divisions, plot_height=450,
                   title="Average Score", toolbar_location=None, tools="")

    # Automatically adjust graph size
    graph.sizing_mode = default_sizing

    source = ColumnDataSource(data=dict(divisions=divisions, div_ave_scores=div_ave_scores))

    labels = LabelSet(x='divisions', y='div_ave_scores', text='div_ave_scores', level='glyph',
                      x_offset=-13.5, y_offset=0, source=source, render_mode='canvas')

    graph.vbar(x='divisions', top='div_ave_scores', width=0.9, source=source)

    graph.y_range.start = 0

    graph.add_layout(labels)
    graph.xaxis.major_label_text_font_size = "15pt"

    # show the results
    #output_file("division_graph.html")
    #show(graph)

    # Remove toolbar from graph
    graph.toolbar_location = None

    return components(graph)


def graph_event_progress(title, dates, scores, averages, metric):
    x_axis_label = 'Date'
    y_axis_label = 'Score' + ' (' + metric + ')'

    graph = figure(x_axis_label=x_axis_label, x_axis_type='datetime',
                   y_axis_label=y_axis_label,
                   title=title + ' (hover mouse over circle to see score)', plot_width=100, plot_height=100)

    # Automatically adjust graph size
    graph.sizing_mode = default_sizing

    # Format axes
    graph.xaxis.formatter = DatetimeTickFormatter(days='%F', months='%F', years='%F')

    # Show data points on hover
    graph.add_tools(HoverTool(tooltips=[('x,y', '@x{%F}, @y')], formatters={'x': 'datetime'}, mode='mouse'))

    # Plot average line
    graph.line(dates, averages, line_color="#C4DAFF", line_width=2, legend='Top score')
    graph.circle(dates, averages, size=10, color="#C4DAFF")

    # Plot athlete line
    graph.line(dates, scores, line_color="#D3C2FF", line_width=2, legend='Average score')
    graph.circle(dates, scores, size=10, color="#D3C2FF")

    # Remove toolbar from graph
    graph.toolbar_location = None

    return components(graph)


def graph_bar_correlation_index(title, correlation):
    graph = figure(x_range=correlation["variable"], plot_height=250, title=title, toolbar_location=None, tools="")

    # Graph vertical bars with color
    color = ['#3288bd', '#99d594', '#e6f598', '#fee08b']
    graph.vbar(x=correlation["variable"], top=correlation["index"], line_color="white", fill_color=color, width=0.9)

    # Hide background grid
    graph.xgrid.visible = False
    graph.ygrid.visible = False

    # Set scale start for y
    graph.y_range.start = 0

    # Automatically adjust graph size
    graph.sizing_mode = default_sizing

    return components(graph)


def graph_pie_sport_origin(title, origin):
    # Manage data with Pandas
    # Based on code found in https://bokeh.pydata.org/en/latest/docs/gallery/pie_chart.html
    data = pd.Series(origin).reset_index(name='value').rename(columns={'index':'country'})
    data['angle'] = data['value']/data['value'].sum() * 2*3.14159
    data['color'] = ['#3288bd', '#99d594', '#e6f598', '#fee08b', '#fc8d59']

    graph = figure(plot_height=350, title=title, toolbar_location=None, tools="hover", tooltips="@country: @value")

    # Graph the pie pieces
    graph.wedge(x=0, y=1, radius=0.4, start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
                line_color="white", fill_color='color', legend='country', source=data)

    # Hide background grid and axis
    graph.axis.visible = False
    graph.xgrid.visible = False
    graph.ygrid.visible = False

    # Automatically adjust graph size
    graph.sizing_mode = default_sizing

    return components(graph)


def graph_lollipop_graph(names, scores):

    graph = figure(title="Individual Goals", tools="", toolbar_location=None,
                 y_range=names, x_range=[0, 15])

    graph.segment(0, names, scores, names, line_width=2, line_color="#C4DAFF", )
    graph.circle(scores, names, size=15, fill_color="#D3C2FF", line_color="#C4DAFF", line_width=3, )

    source = ColumnDataSource(data=dict(scores=scores, names=names))

    labels = LabelSet(x='scores', y='names', text='scores', level='glyph',
                      x_offset=-13.5, y_offset=0, source=source, render_mode='canvas')

    graph.add_layout(labels)

    # Automatically adjust graph size
    graph.sizing_mode = "fixed"

    return components(graph)

# reference: https://python-graph-gallery.com/161-custom-matplotlib-donut-plot/
def graph_donut_graph(label):
    names = "Won", "Lost", "Tied"
    size = [38, 16, 13]
    centre = plt.Circle((0, 0), 0.7, color='white')
    if label == "Won":
        plt.pie(size, labels=names, colors=['skyblue', 'lightgrey', 'lightgrey'], textprops={'fontsize': 40})
        p = plt.gcf()
        p.gca().add_artist(centre)
        plt.savefig("../static/won.jpg")
    elif label == "Lost":
        plt.pie(size, labels=names, colors=['lightgrey', 'blue', 'lightgrey'], textprops={'fontsize': 40})
        p = plt.gcf()
        p.gca().add_artist(centre)
        plt.savefig("../static/lost.jpg")
    else:
        plt.pie(size, labels=names, colors=['lightgrey', 'lightgrey', 'royalblue'], textprops={'fontsize': 40})
        p = plt.gcf()
        p.gca().add_artist(centre)
        plt.savefig("../static/tied.jpg")


if __name__ == '__main__':
    graph_power_lifting_relative_personal_best([109.4, 88.0, 109.0], [98.2, 66.7, 82.2], ["Bench Press", "Deadlift", "Squat"])

    names = ["a", "b", "c", "d", "e", "f", "g", "h"]
    scores = [50, 40, 65, 10, 25, 37, 80, 60]

    graph_lollipop_graph(names, scores)
