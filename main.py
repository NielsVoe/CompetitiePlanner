from src.ToernooiHandler import ToernooiHandler
from src.Club import Club
from src.Team import Team
from src.Player import Player
from src.Gender import Gender

def main():
    competitie = ToernooiHandler("https://badmintonnederland.toernooi.nl/sport/clubs.aspx?id=B1A6EFC2-20ED-499C-8EF0-07D734E0B4B7")
    clubID = competitie.GetClubID("GELDROP BC").split("?", 1)[-1]
    club = Club("GELDROP BC", clubID, 10)
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
            team.AddPlayer(player)
        club.AddTeam(team)
    
    for team in club.teams:
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
    main()