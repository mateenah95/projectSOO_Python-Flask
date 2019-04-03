import requests


def get_athlete(athlete_name):
    athlete_name = athlete_name.lower()
    athlete_name = athlete_name.replace(' ', '_')
    server = 'http://138.197.152.213/'

    response = requests.get(server + athlete_name)

    if len(response.content) > 0:
        return response.json()
    else:
        return {}


def get_team(team_name):
    team_name = team_name.lower()
    server = 'http://138.197.152.213/'
    team_jsons = {}

    soccerTeam = {
        "name": "Toronto",
        "teamID": 10023,
        "teamIcon": "",
        "province": "Ontario",
        "sport": "soccer",
        "played": 67,
        "won": 38,
        "lost": 16,
        "drawn": 13,
        "goalsScored": 101,
        "goalsConceded": 27,
        "totalShots": 123,
        "shotsOnTarget": 32,
        "totalSaves": 28,
        "cleanSheets": 14,
        "totalFowls": 19,
        "yellowCards": 7,
        "redCards": 2,
        "coach": "John Doe",
        "roster": [
            ["Milan Borjan", 12, 0, "GoalKeeper"], ["Zachary Brault-Guillard", 8, 4, "Defender"],
            ["Alessandro Busti", 6, 7, "Defender"], ["Marco Bustos", 11, 9, "Defender"],
            ["Lucas Cavallini", 23, 4, "Defender"], ["Jay Chapman", 12, 3, "Midfielder"],
            ["Juan Córdova", 17, 2, "Midfielder"], ["Derek Cornelius", 10, 10, "midfielder"],
            ["Maxime Crépeau", 15, 3, "Midfielder"], ["Jonathan David", 2, 6, "Striker"],
            ["Alphonso Davies", 4, 5, "Striker"]
        ]

    }

    softballTeam = {
        "name": "Mississauga",
        "teamID": 10087,
        "teamIcon": "",
        "province": "Ontario",
        "sport": "softball",
        "games": 24,
        "runs": 176,
        "hits": 249,
        "atBat": 703,
        "hr": 11,
        "streak": 7,
        "home": "9-3",
        "away": "8-4",
        "neutral": "0-0",
        "singles": 122,
        "doubles": 47,
        "triples": 13,
        "onBase": 0.406,
        "batAvg": 0.354,
        "walks": 56,
        "strikeOut": 100,
        "shutOut": 5,
        "bases": 343,
        "roster": [
            ["Anissa Zacharczuk", 12, "5-8", "P/UT"], ["Chelsea Hotner", 8, "5-5", "OF"],
            ["Georgia Ogg", 6, "5-2", "C/OF"], ["Rebecca Kirkpatrick", 11, "5-4", "INF"],
            ["Courtney De Adder", 23, "5-6", "INF"], ["Bonnie Whitford", 12, "5-6", "CF"],
            ["Kate Fergusson", 17, "5-9", "1B/OF"], ["Maria Seminario", 10, "5-5", "OF"],
            ["Samantha Ruffett", 15, "5-9", "1B/C"], ["Jessica Fasolino", 2, "5-7", "p"],
            ["Kendra Ho", 4, "5-5", "P"]
        ]
    }
    response = []
    if team_name.lower() == "toronto":
        response = [soccerTeam]
    elif team_name.lower() == "mississauga":
        response = [softballTeam]

    return response
