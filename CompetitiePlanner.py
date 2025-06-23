from src.ToernooiHandler import ToernooiHandler
from src.Club import Club
from src.Team import Team
from src.Player import Player
from src.Gender import Gender

club = Club("GELDROP BC", 10)
url = "https://badmintonnederland.toernooi.nl/sport/clubs.aspx?id=B1A6EFC2-20ED-499C-8EF0-07D734E0B4B7"

def GetUrl() -> str:
    return url

def RetrieveData():
    competitie = ToernooiHandler(url)
    clubID = competitie.GetClubID("GELDROP BC").split("?", 1)[-1]
    club.SetClubID(clubID)
    teams = competitie.GetTeams(clubID)
    for t in teams:
        teamID = t["ID"]
        team = Team(t["Team"], teamID)
        players = competitie.GetPlayers(teamID)
        for p in players:
            playerID = p["ID"]
            vastSpeler = p["VastSpeler"]
            playerName = p["Name"]
            gender = Gender.MALE if p["Gender"] == "Male" else Gender.FEMALE
            player = Player(playerName, playerID, gender)
            if vastSpeler:
                team.AddPlayer(player)
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