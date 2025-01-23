

class TeamName:
    
    id: int
    franchise_id: int
    full_name: str
    league_id: int
    abrv: str
    
    def __init__(self, id: int, franchiseId: int, fullName: str, leagueId: int, triCode: str):
        self.id = id
        self.franchise_id = franchiseId
        self.full_name = fullName
        self.league_id = leagueId
        self.abrv = triCode
        
        
    def __repr__(self):
        return f"{self.tricode} - {self.full_name} - {self.id}"
    
    
class Team:
    
    id: int
    franchise_id: int
    full_name: str
    league_id: int
    abrv: str
    common_name: str
    place_name: str
    logo_url: str
    logo_url_dark: str
    
    def __init__(self, team_name: TeamName, common_name: str, place_name: str, logo_url: str, logo_url_dark: str):
        self.id = team_name.id
        self.franchise_id = team_name.franchise_id
        self.full_name = team_name.full_name
        self.league_id = team_name.league_id
        self.abrv = team_name.abrv
        self.common_name = common_name
        self.place_name = place_name
        self.logo_url = logo_url
        self.logo_url_dark = logo_url_dark
        
    def __repr__(self):
        return f"{self.id} - {self.abrv} - {self.full_name} - {self.common_name} - {self.place_name}"
    
class Game_Schedule:
    
    id: int
    season_id: int
    date: str
    venue: str
    away_team_id: int
    home_team_id: int
        

