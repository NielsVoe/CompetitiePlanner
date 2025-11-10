from src.Team import Team
from src.Serialize import Serialize

class Club(Serialize):
    def __init__(self, name:str, courtsAvailable:int, id:str=""):
        self.name = name
        self.id = id
        self.courtsAvailable = courtsAvailable
        self.teams:list[Team] = []

    def Reset(self):
        self.teams.clear()
    
    def SetClubID(self, id:str):
        self.id = id

    def GetTeams(self) -> list[Team]:
        print(f"Number of teams in club {self.name}: {len(self.teams)}")
        return self.teams
    
    def GetSingleTeam(self, teamName:str) -> Team:
        for team in self.teams:
            if team.name == teamName:
                return team
        return None

    def AddTeam(self, team:Team) -> bool:
        if team in self.teams:
            return False
        if team.name in [t.name for t in self.teams]:
            raise ValueError(f"Team with name {team.name} already exists in club {self.name}.")
        self.teams.append(team)
        return True
    
    def ToDict(self):
        return {
            "name": self.name,
            "id": self.id,
            "courtsAvailable": self.courtsAvailable,
            "teams": [team.ToDict() for team in self.teams]
        }