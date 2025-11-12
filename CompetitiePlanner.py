from src.ToernooiHandler import ToernooiHandler
from src.Club import Club
from src.Team import Team
from src.Player import Player
from src.Gender import Gender
from src.Teammatch import Teammatch

club = Club("GELDROP BC", 9)

def ResetClub():
    club.Reset()

def RetrieveData(url):
    competitie = ToernooiHandler(url)
    clubID = competitie.GetClubID("GELDROP BC").split("?", 1)[-1]
    club.SetClubID(clubID)
    teams = competitie.GetTeams(clubID)
    for t in teams:
        teamID = t["ID"]
        team = Team(t["Team"], teamID)
        for p in competitie.GetPlayers(teamID):
            playerID = p["ID"]
            vastSpeler = p["VastSpeler"]
            playerName = p["Name"]
            gender = Gender.MALE if p["Gender"] == "Male" else Gender.FEMALE
            player = Player(playerName, playerID, gender)
            if vastSpeler:
                if not team.AddPlayer(player):
                    raise ValueError(f"Player with name {player.name} already exists in team {team.name}.")
        for m in competitie.GetMatches(teamID):
            matchDate = m["Date"]
            home = m["Home"]
            away = m["Away"]
            try:
                resultHome = m["Result"].split("-")[0].strip()
                resultAway = m["Result"].split("-")[1].strip()
            except ValueError:
                resultHome = ""
                resultAway = ""
            match = Teammatch(home, away, resultHome, resultAway, matchDate)
            if not team.AddMatch(match):
                raise ValueError(f"Match {match} already exists in team {team.name}.")
        try:
            club.AddTeam(team)
        except ValueError as ve:
            existingTeam = club.GetSingleTeam(team.name)
            if existingTeam is None:
                raise ValueError(f"Team {team.name} not found in club")
            existingTeam.AddPlayers(team.GetPlayers())
            existingTeam.AddMatches(team.GetMatches())

def GetClub():
    return club

def PrintData():
    team:Team
    teams = club.GetTeams()
    for team in teams:
        print(f"Team: {team.name}")
        print(f"  Heren:")
        for player in team.players:
            if player.gender == Gender.MALE:
                print(player.name)
        print(f"  Dames:")
        for player in team.players:
            if player.gender == Gender.FEMALE:
                print(player.name)

if __name__ == "__main__":
    RetrieveData()
    PrintData()