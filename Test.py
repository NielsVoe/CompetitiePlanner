# This is a test file for the Python script.
from src.ToernooiHandler import ToernooiHandler
url = "https://badmintonnederland.toernooi.nl/sport/clubs.aspx?id=39A69CCC-55A7-47C2-A19C-E41728508953"
teamID = "id=39A69CCC-55A7-47C2-A19C-E41728508953&tid=375"
competitie = ToernooiHandler(url)

matches = competitie.GetMatches(teamID)
for match in matches:
    print(f"Date: {match['Date']}")
    print(f"Home: {match['Home']}")
    print(f"Away: {match['Away']}")
    print(f"Result: {match['Result']}")