from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

# Global date format
date_format = '%Y-%m-%d'


def get_athlete_name(athlete):
    name = ''
    name_list = athlete['name']

    for i in range(len(name_list)):
        if len(name_list[i]) > 0:
            name += name_list[i] + ' '

    name.strip()
    return name


def get_athlete_sport(athlete):
    return athlete['sport']


def get_athlete_age(athlete):
    dob = datetime.strptime(athlete['DOB'], date_format)
    today = datetime.today()
    age = relativedelta(today, dob).years

    return age


def get_athlete_province(athlete):
    return athlete['province']


def get_competition_date(athlete, competition):
    return athlete['competitions'][competition]['date']


def get_athlete_progress(athlete, event):
    competitions = athlete['results'][event]

    dates = []
    scores = []

    for competition in competitions:
        date = get_competition_date(athlete, competition)
        dates.append(datetime.strptime(date, date_format))
        scores.append(competitions[competition]['score'])

    return dates, scores


def convert_seconds_to_minutes_seconds_milliseconds(seconds):
    converted = str(timedelta(seconds=seconds))

    hours_minutes_seconds = converted.split(':')
    seconds_milliseconds = hours_minutes_seconds[2].split('.')

    minutes = hours_minutes_seconds[1]
    seconds = seconds_milliseconds[0]

    if len(seconds_milliseconds) > 1:
        milliseconds = seconds_milliseconds[1][0:2]
    else:
        milliseconds = '00'

    minutes_seconds = ':'.join([minutes, seconds])
    minutes_seconds_milliseconds =':'.join([minutes_seconds, milliseconds])

    # Trim off hours from the string
    return minutes_seconds_milliseconds


def get_swimming_top_three_results(athlete, event):
    results = athlete['results'][event]

    event_results = []

    for competition in results:
        event_results.append((competition, results[competition]))

    sorted_event_results = (sorted(event_results, key=lambda x: x[1]['score']))

    top_three = sorted_event_results[0:3]
    return top_three


def get_swimming_personal_best(athlete, event):
    personal_best_event = athlete['personal best'][event]
    record = personal_best_event['record']
    percentile = personal_best_event['percentile']

    return convert_seconds_to_minutes_seconds_milliseconds(record), percentile


def get_swimming_results_table(athlete, event):
    results_table = []

    # A list of ordered tuples, (<competition name>, <competition results>)
    top_three_competitions = get_swimming_top_three_results(athlete, event)

    for i in range(0, 3):
        competition_result = {}
        time = top_three_competitions[i][1]['score']
        rank = top_three_competitions[i][1]['rank']

        competition_result['title'] = top_three_competitions[i][0]
        competition_result['time'] = convert_seconds_to_minutes_seconds_milliseconds(time)
        competition_result['rank'] = rank

        results_table.append(competition_result)

    return results_table


def get_power_lifting_personal_best(athlete, event):
    personal_best = athlete['personal best'][event]

    division = personal_best['division']
    record = personal_best['record']
    division_average = personal_best['division average']

    return division, record, division_average


def get_power_lifting_personal_best_all_events(athlete):
    personal_best = athlete['personal best']

    scores = []
    averages = []
    index = []

    for event in personal_best:
        index.append(event)
        scores.append(personal_best[event]['record'])
        averages.append(personal_best[event]['division average'])

    return scores, averages, index


def get_power_lifting_results_table(athlete):
    results_table = []

    competitions = athlete['competitions']
    results = athlete['results']

    for competition in competitions:
        competition_result = {}
        bench_press_score = results['bench press'][competition]['score']
        deadlift_score = results['deadlift'][competition]['score']
        squat_score = results['squat'][competition]['score']

        competition_result['competition'] = competition
        competition_result['ranking'] = competitions[competition]['rank']
        competition_result['bench press'] = bench_press_score
        competition_result['deadlift'] = deadlift_score
        competition_result['squat'] = squat_score
        competition_result['total'] = bench_press_score + deadlift_score + squat_score

        results_table.append(competition_result)

    return results_table


def get_event_number(sport):
    return sport['eventNum']


def get_event_names(sport):
    events = sport["events"]
    event_names = []
    i = 0
    while i < get_event_number(sport):
        event_names.append(events[i]["name"][3:])
        i += 1

    return event_names


def get_top_scores(event):
    scores = []
    top_three = event["topThree"]

    i = 0
    while i < 3:
        scores.append(top_three[i]["score"])
        i += 1

    return scores


def get_top_athletes(event):
    athletes = []
    top_three = event["topThree"]

    i = 0
    while i < 3:
        athletes.append(top_three[i]["athlete"])
        i += 1

    return athletes


def get_division_average(event):
    # for bar graph
    divisions = event["divisions"]
    ave_scores = event["DivAveScores"]

    return divisions, ave_scores


def get_year_score(event):
    results = event["results"]
    top = []
    average = []
    dates = []
    i = 0
    while i < len(results):
        dates.append(datetime.strptime(results[i]['date'], date_format))
        top.append(results[i]["top"])
        average.append(results[i]["average"])
        i += 1

    return top, average, dates


def get_player_name_position(team, i):
    player = team["roster"][i]
    name = player[0]
    back_number = player[1]
    goals = player[2]
    position = player[3]

    return name, back_number, goals, position


def get_soccer_team_names_scores(team):
    players = team["roster"]
    names = []
    scores = []

    i = 0
    while i < len(players):
        names.append(players[i][0])
        scores.append(players[i][2])
        i += 1

    return names, scores
