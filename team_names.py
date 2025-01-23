from models import TeamName, Team
import requests
from string import Template

endpoint_team_names = 'https://api.nhle.com/stats/rest/en/team'
endpoint_team_meta_info = Template('https://api-web.nhle.com/v1/club-schedule-season/$abrv/$season')

endpoints = {
    'team_names': 'https://api.nhle.com/stats/rest/en/team',
    'team_meta_info': Template('https://api-web.nhle.com/v1/club-schedule-season/$abrv/$season')
}

def get_team_info():
    team_names = get_team_names()
    team_info = get_team_meta_info([20202021], team_names)
    return team_info

def get_team_names():
    response = requests.get(endpoints['team_names'])
    response.raise_for_status()
    data = response.json()
    names = data['data']
    team_names = [TeamName(name['id'], name['franchiseId'],
                                  name['fullName'], name['leagueId'], 
                                  name['triCode']) for name in names]

    return team_names

def get_team_meta_info(seasons: list, teams: list):
    full_team_info = []
    for team in teams:
        for season in seasons:
            url = endpoints['team_meta_info'].substitute(abrv=team.abrv, season=season)
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if len(data['games']) == 0:
                continue
            first_game = data['games'][0]
            away_team = first_game['awayTeam']
            home_team = first_game['homeTeam']
            this_team =away_team if away_team['abbrev'] == team.abrv else home_team
            team_info = Team(team, 
                             this_team['commonName'].get('default'),
                             this_team['placeName'].get('default'),
                             this_team['logo'], this_team['darkLogo'])
            full_team_info.append(team_info)
    
    return full_team_info


teams = get_team_info()

for team in teams:
    print(team)