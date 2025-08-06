from httpx import Client
from bs4 import BeautifulSoup
from src.Format import Format
from src.Date import Date

HEADERS = {"Cookie": "_ga=GA1.1.1888592977.1711484788; BCSessionID=266b900f-096a-4eb5-87b3-0af16b3db006; _ga_4BZBWY18RJ=GS1.1.1711484788.1.1.1711485972.0.0.0; lvt=vJK7Ne8BzsVEGOZLKjAvV95Eph2N8YkVcFYVST9yqklfBM357xCtt1jMBMT2j0RZUH0wDeZdsoM=; st=l=1043&exp=46070.9212847685&c=1&cp=31&s=2; .ASPX_TOURNAMENT_WEBSITE=5FAEFEB99D5E427343F0BB7C77EA92C25E0A87BAD57643FBE4978656DBF9AE0CE40329915240D1D323F5460597D08D244CE9C9578F8043214EF9960698E1237E399B44AFFE5D22829856CA2263AC3EFB1826761B; ASP.NET_SessionId=fwo3ddc2hymtyzlnanoyojtw"}

class ToernooiHandler:
    def __init__(self, url:str):
        self.url = url

    def GetClubID(self, clubName:str) -> str:
        # Get the link to the club page from the club name
        # The club name is the name of the club in the url
        # The url is the link to the club page
        with Client(headers=HEADERS) as client:
            response = client.get(self.url)
            soup = BeautifulSoup(response.text, "html.parser")
            for table in soup.select(".ruler"):
                for row in table.select("tr"):
                    if row.select("td")[0].text == clubName:
                        return row.select("a")[0]["href"]
        return None
    
    def GetTeams(self, clubID:str) -> list:
        # Get the teams from the club page
        # The club ID is the id of the club in the url
        # The url is the link to the club page

        link = f"https://badmintonnederland.toernooi.nl/sport/clubteams.aspx?{clubID}"

        with Client(headers=HEADERS) as client:
            response = client.get(link)
            soup = BeautifulSoup(response.text, "html.parser")
            teams = []
            for table in soup.select(".clublist.clubteams.ruler"):
                for row in table.select("tr"):
                    if row.select("td")[0].text != "":
                        if "GELDROP BC" in row.select("td")[0].text:
                            team = row.select("td")[0].text
                            id = row.select("a")[0]["href"].split("?", 1)[-1]
                            teams.append({"Team": team, "ID": id})
            return teams
    
    def GetPlayers(self, teamID:str) -> list:
        # Get the players from the team page
        # The team ID is the id of the team in the url
        # The url is the link to the team page

        link = f"https://badmintonnederland.toernooi.nl/sport/teamplayers.aspx?{teamID}"

        with Client(headers=HEADERS) as client:
            response = client.get(link)
            soup = BeautifulSoup(response.text, "html.parser")
            players = []
            for table in soup.select(".teamplayerlists"):
                for males in table.select(".maleplayers"):
                    for tr in males.select("tr"):
                        vastSpeler = "Nee"
                        for td in tr.select("td"):
                            if td.text == "Ja":
                                vastSpeler = "Ja"
                        for male in tr.select("#playercell"):
                            name = Format.Name(male.select("a")[0].text)
                            id = male.select("a")[0]["href"].split("?", 1)[-1]
                            players.append({"Name": name, "ID": id, "VastSpeler": vastSpeler, "Gender": "Male"})
                for females in table.select(".femaleplayers"):
                    for tr in females.select("tr"):
                        vastSpeler = "Nee"
                        for td in tr.select("td"):
                            if td.text == "Ja":
                                vastSpeler = "Ja"
                        for female in tr.select("#playercell"):
                            name = Format.Name(female.select("a")[0].text)
                            id = female.select("a")[0]["href"].split("?", 1)[-1]
                            players.append({"Name": name, "ID": id, "VastSpeler": vastSpeler, "Gender": "Female"})
            return players
        
    def GetMatches(self, teamID:str) -> list:
        # Get the matches from the team page
        # The team ID is the id of the team in the url
        # The url is the link to the team page

        link = f"https://badmintonnederland.toernooi.nl/sport/teammatches.aspx?{teamID}"

        with Client(headers=HEADERS) as client:
            response = client.get(link)
            soup = BeautifulSoup(response.text, "html.parser")
            matches = []
            for div in soup.select(".teammatch-table"):
                for table in div.select("tbody"):
                    for tr in table.select("tr"):
                        td = tr.find_all("td")
                        parts = td[1].text.split(" ")
                        date = Date(day=parts[0], date=parts[1], time=parts[2])
                        match = {
                            "Date": date,
                            "Home": td[6].text,
                            "Away": td[8].text,
                            "Result": td[9].text,
                        }
                        matches.append(match)
            return matches