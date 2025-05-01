from src.ToernooiHandler import ToernooiHandler

def main():
    print("Welcome to the Competitie Planner!")

if __name__ == "__main__":
    main()
    competitie = ToernooiHandler("https://badmintonnederland.toernooi.nl/sport/clubs.aspx?id=B1A6EFC2-20ED-499C-8EF0-07D734E0B4B7")
    clubID = competitie.GetClubID("GELDROP BC").split("?", 1)[-1]
    teams = competitie.GetTeams(clubID)