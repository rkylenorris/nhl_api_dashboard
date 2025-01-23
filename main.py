from models import Team
import requests
import json
from string import Template

def get_teams():
    endpoint = 'https://api.nhle.com/stats/rest/en/team'
    response = requests.get(endpoint)
    response.raise_for_status()
    data = response.json()
    teams = data['data']
    team_objs = []
    for team in teams:
        team_objs.append(Team(**team))

    return team_objs

teams = get_teams()
for team in teams:
    print(team)
    
def get_schedule(seasons: list, teams: list):
    endpoint = Template('https://api-web.nhle.com/v1/club-schedule-season/$tricode/$season')
    for team in teams:
        for season in seasons:
            url = endpoint.substitute(tricode=team.tricode, season=season)
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            print(data)