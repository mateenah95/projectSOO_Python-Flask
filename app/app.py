from flask import Flask, render_template, redirect, request, jsonify, url_for
import requests

from parse import *
from graph import *
from athlete_factory import *

app = Flask(__name__, template_folder="../templates", static_folder="../static")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search_query', methods=['POST'])
def search_query():
    search_request = request.get_json()

    # Response is a list of dicts
    response = []

    if search_request['type'].lower() == 'player':
        response_json = get_athlete(search_request['name'])

        if len(response_json) > 0:
            athlete_name = get_athlete_name(response_json)
            athlete_province = get_athlete_province(response_json)
            athlete_sport = get_athlete_sport(response_json)
            response.append({'name': athlete_name, 'province': athlete_province, 'sport': athlete_sport})

    elif search_request['type'].lower() == 'team':
        response_json = get_team(search_request['name'])

        for item in response_json:
            response.append({'name': item["name"], 'province': item["province"], 'sport': item["sport"]})
            response.append({'name': item["name"], 'province': item["province"], 'sport': item["sport"]})

    return jsonify(response)



@app.route('/search')
def search():
    return render_template('search_page.html')

@app.route('/player/<name>', methods=['GET', 'POST'])
def player(name):
    # Get athlete json from mock server
    athlete_json = get_athlete(name)

    if get_athlete_sport(athlete_json) == 'Power Lifting':
        return render_power_lifting_page(athlete_json)
    elif get_athlete_sport(athlete_json) == 'Swimming':
        return render_swimming_page(athlete_json)


def render_power_lifting_page(athlete_json):
    name = get_athlete_name(athlete_json)
    age = get_athlete_age(athlete_json)
    province = get_athlete_province(athlete_json)
    sport = get_athlete_sport(athlete_json)

    dates, scores = get_athlete_progress(athlete_json, 'bench press')
    div1, script1 = graph_athlete_progress(dates, scores)

    dates, scores = get_athlete_progress(athlete_json, 'squat')
    div2, script2 = graph_athlete_progress(dates, scores)

    dates, scores = get_athlete_progress(athlete_json, 'deadlift')
    div3, script3 = graph_athlete_progress(dates, scores)

    firstname, lastname = name.split(' ')[0:2]
    athlete_image = url_for('static', filename='img/'+firstname+'_'+lastname+'.png')

    bench_press_division, bench_press_record, bench_press_average = get_power_lifting_personal_best(athlete_json, 'bench press')
    deadlift_division, deadlift_record, deadlift_average = get_power_lifting_personal_best(athlete_json, 'deadlift')
    squat_division, squat_record, squat_average = get_power_lifting_personal_best(athlete_json, 'squat')

    # # Create radar graph
    scores, averages, index = get_power_lifting_personal_best_all_events(athlete_json)
    graph_power_lifting_relative_personal_best(scores, averages, index)

    # Return results table info, a list of dicts
    competition_results = get_power_lifting_results_table(athlete_json)

    return render_template('player.html', **locals())


def render_swimming_page(athlete_json):
    name = get_athlete_name(athlete_json)
    age = get_athlete_age(athlete_json)
    province = get_athlete_province(athlete_json)
    sport = get_athlete_sport(athlete_json)

    firstname, lastname = name.split(' ')[0:2]
    athlete_image = url_for('static', filename='img/'+firstname+'_'+lastname+'.png')

    events_graphs = []
    for event in athlete_json['results']:
        dates, scores = get_athlete_progress(athlete_json, event)
        div, script = graph_athlete_progress(dates, scores)
        events_graphs.append([div, script])

    events_progress = []
    for event in athlete_json['results']:
        event_progress = {}
        record, percentile = get_swimming_personal_best(athlete_json, event)
        results_table = get_swimming_results_table(athlete_json, event)

        event_progress['title'] = event
        event_progress['record'] = record
        event_progress['percentile'] = percentile
        event_progress['results table'] = results_table

        events_progress.append(event_progress)

    return render_template('player.html', **locals())


@app.route('/sports')
def sports_main():
    return render_template('sports_main.html')


@app.route('/sports/<sport>')
def sports(sport):

    # Get swimming sport json from mock server
    mock = 'http://138.197.152.213/'
    json = requests.get(mock+sport).json()

    title = json["sport"]["name"]
    banner = 'img/'+title+'-banner.jpg'
    banner_image = url_for('static', filename=banner)

    athlete1_name = json["athletes"][0]["name"]
    athlete1_gold = json["athletes"][0]["medal"][0]
    athlete1_silver = json["athletes"][0]["medal"][1]
    athlete1_bronze = json["athletes"][0]["medal"][2]
    call = athlete1_name.split(" ")
    athlete1_image = url_for('static', filename='img/'+call[0]+'_'+call[1]+'.png')
    athlete1_link = url_for('player', name=call[0]+'_'+call[1])
    if athlete1_name == 'Toronto ':
        athlete1_link = '/team/soccer/toronto'

    athlete2_name = json["athletes"][1]["name"]
    athlete2_gold = json["athletes"][1]["medal"][0]
    athlete2_silver = json["athletes"][1]["medal"][1]
    athlete2_bronze = json["athletes"][1]["medal"][2]
    call = athlete2_name.split(" ")
    athlete2_image = url_for('static', filename='img/' + call[0] + '_' + call[1] + '.png')
    athlete2_link = url_for('player', name=call[0] + '_' + call[1])
    if athlete2_name[-1] == ' ':
        athlete2_link = '/team/soccer/toronto'

    athlete3_name = json["athletes"][2]["name"]
    athlete3_gold = json["athletes"][2]["medal"][0]
    athlete3_silver = json["athletes"][2]["medal"][1]
    athlete3_bronze = json["athletes"][2]["medal"][2]
    call = athlete3_name.split(" ")
    athlete3_image = url_for('static', filename='img/' + call[0] + '_' + call[1] + '.png')
    athlete3_link = url_for('player', name=call[0] + '_' + call[1])
    if athlete3_name[-1] == ' ':
        athlete3_link = '/team/soccer/toronto'

    athlete4_name = json["athletes"][3]["name"]
    athlete4_gold = json["athletes"][3]["medal"][0]
    athlete4_silver = json["athletes"][3]["medal"][1]
    athlete4_bronze = json["athletes"][3]["medal"][2]
    call = athlete4_name.split(" ")
    athlete4_image = url_for('static', filename='img/' + call[0] + '_' + call[1] + '.png')
    athlete4_link = url_for('player', name=call[0] + '_' + call[1])
    if athlete4_name[-1] == ' ':
        athlete4_link = '/team/soccer/toronto'

    athlete5_name = json["athletes"][4]["name"]
    athlete5_gold = json["athletes"][4]["medal"][0]
    athlete5_silver = json["athletes"][4]["medal"][1]
    athlete5_bronze = json["athletes"][4]["medal"][2]
    call = athlete5_name.split(" ")
    athlete5_image = url_for('static', filename='img/' + call[0] + '_' + call[1] + '.png')
    athlete5_link = url_for('player', name=call[0] + '_' + call[1])
    if athlete5_name[-1] == ' ':
        athlete5_link = '/team/soccer/toronto'

    script1, div1 = graph_bar_correlation_index(title + " Performance Correlation Index", json["graph"]["correlation"])
    script2, div2 = graph_pie_sport_origin(title + " athletes by Province", json["graph"]["location"])

    return render_template('sport_base.html', **locals())

@app.route('/competition')
def competition():
    sport_name = "Swimming"
    event_name = '100 Backstroke'
    competition1 = "Ontario 2012 Comeptition"
    competition2 = "Ontario 2013 Comeptition"

    # graph first bar chart
    division = ["F1", "F2", "F3", "M1", "M2", "M3"]

    ave1 = ["63.2", "70.8", "105.6", "58.8", "60.9", "71.3"]
    div1, script1 = graph_compare_divisions(division, ave1)

    ave2 = ["65.3", "96.8", "107.6", "60.8", "72.6", "86.5"]
    div2, script2 = graph_compare_divisions(division, ave2)

    return render_template('competition.html', **locals())


@app.route('/team/softball/<team_name>')
def team_softball(team_name):
    mock = "http://138.197.152.213/"
    team = requests.get(mock + "mississauga").json()

    team_name = team["name"]
    province = team["province"]
    team_sport = team["sport"]
    games = team["games"]
    runs = team["runs"]
    hits = team["hits"]
    atBat = team["atBat"]
    hr = team["hr"]
    streak = team["streak"]
    home = team["home"]
    away = team["away"]
    neutral = team["neutral"]
    singles = team["singles"]
    doubles = team["doubles"]
    triples = team["triples"]
    onBase = team["onBase"]
    batAvg = team["batAvg"]
    walks = team["walks"]
    strikeOut = team["strikeOut"]
    shutOut = team["shutOut"]
    bases = team["bases"]

    name1, back_number1, ht1, position1 = get_player_name_position(team, 0)
    name2, back_number2, ht2, position2 = get_player_name_position(team, 1)
    name3, back_number3, ht3, position3 = get_player_name_position(team, 2)
    name4, back_number4, ht4, position4 = get_player_name_position(team, 3)
    name5, back_number5, ht5, position5 = get_player_name_position(team, 4)
    name6, back_number6, ht6, position6 = get_player_name_position(team, 5)
    name7, back_number7, ht7, position7 = get_player_name_position(team, 6)
    name8, back_number8, ht8, position8 = get_player_name_position(team, 7)
    name9, back_number9, ht9, position9 = get_player_name_position(team, 8)
    name10, back_number10, ht10, position10 = get_player_name_position(team, 9)
    name11, back_number11, ht11, position11 = get_player_name_position(team, 10)
    return render_template('team_softball.html', **locals())


@app.route('/team/soccer/<team_name>')
def team_soccer(team_name):
    # Get the team json from the mock server
    mock = "http://138.197.152.213/"
    team = requests.get(mock + "toronto").json()

    team_name = team["name"]
    province = team["province"]
    team_sport = team["sport"]
    coach = team["coach"]
    games_played = team["played"]
    games_won = team["won"]
    games_lost = team["lost"]
    games_drawn = team["drawn"]
    goals_scored = team["goalsScored"]
    goals_conceded = team["goalsConceded"]
    total_shots = team["totalShots"]
    shots_on_target = team["shotsOnTarget"]
    total_saves = team["totalSaves"]
    clean_sheets = team["cleanSheets"]
    total_fowls = team["totalFowls"]
    yellow_cards = team["yellowCards"]
    red_cards = team["redCards"]
    coach = team["coach"]

    name1, back_number1, goals1, position1 = get_player_name_position(team, 0)
    name2, back_number2, goals2, position2 = get_player_name_position(team, 1)
    name3, back_number3, goals3, position3 = get_player_name_position(team, 2)
    name4, back_number4, goals4, position4 = get_player_name_position(team, 3)
    name5, back_number5, goals5, position5 = get_player_name_position(team, 4)
    name6, back_number6, goals6, position6 = get_player_name_position(team, 5)
    name7, back_number7, goals7, position7 = get_player_name_position(team, 6)
    name8, back_number8, goals8, position8 = get_player_name_position(team, 7)
    name9, back_number9, goals9, position9 = get_player_name_position(team, 8)
    name10, back_number10, goals10, position10 = get_player_name_position(team, 9)
    name11, back_number11, goals11, position11 = get_player_name_position(team, 10)

    graph_donut_graph("Won")
    graph_donut_graph("Lost")
    graph_donut_graph("Tied")

    names, scores = get_soccer_team_names_scores(team)
    script1, div1 = graph_lollipop_graph(names, scores)

    return render_template('team_soccer.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
