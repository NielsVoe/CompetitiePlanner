from src.ToernooiHandler import ToernooiHandler
from src.Club import Club
from src.Team import Team
from src.Player import Player
from src.Gender import Gender
from src.Teammatch import Teammatch

club = Club("GELDROP BC", 9)
url = "https://badmintonnederland.toernooi.nl/sport/clubs.aspx?id=39A69CCC-55A7-47C2-A19C-E41728508953"

def GetUrl() -> str:
    return url

def RetrieveData():
    competitie = ToernooiHandler(url)
    clubID = competitie.GetClubID("GELDROP BC").split("?", 1)[-1]
    club.SetClubID(clubID)
    teams = competitie.GetTeams(clubID)
    club.Reset()
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
                team.AddPlayer(player)
        for m in competitie.GetMatches(teamID):
            matchDate = m["Date"]
            home = m["Home"]
            away = m["Away"]
            result = m["Result"]
            match = Teammatch(home, away, result, result, matchDate)
            if not team.AddMatch(match):
                print(f"Match {match} already exists in team {team.name}")
        club.AddTeam(team)

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