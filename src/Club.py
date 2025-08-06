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
        return self.teams

    def AddTeam(self, team:Team) -> bool:
        if team in self.teams:
            return False
        self.teams.append(team)
        return True
    
    def ToDict(self):
        return {
            "name": self.name,
            "id": self.id,
            "courtsAvailable": self.courtsAvailable,
            "teams": [team.ToDict() for team in self.teams]
        }