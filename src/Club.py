from src.Team import Team

class Club:
    def __init__(self, name:str, id:str, courtsAvailable:int):
        self.name = name
        self.id = id
        self.courtsAvailable = courtsAvailable
        self.teams:list[Team] = []

    def GetTeams(self) -> list[Team]:
        return self.teams

    def AddTeam(self, team:Team) -> bool:
        if team in self.teams:
            return False
        self.teams.append(team)
        return True