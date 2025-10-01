from src.Serialize import Serialize
from src.Date import Date
from datetime import datetime

class Teammatch(Serialize):
    def __init__(self, team1: str, team2: str, score1: int, score2: int, date:Date = None):
        self.team1 = team1
        self.team2 = team2
        self.score1 = score1
        self.score2 = score2
        self.date = date

    def GetHomeTeam(self) -> str:
        return self.team1
    def GetAwayTeam(self) -> str:
        return self.team2
    def GetScore(self) -> tuple[int, int]:
        return self.score1, self.score2
    def GetDay(self) -> str:
        return self.date.GetDay()
    def GetDate(self) -> datetime.date:
        return self.date.GetDate().date()
    def GetTime(self) -> str:
        return self.date.GetTime()
    def __str__(self) -> str:
        return f"{self.date}: {self.team1} vs {self.team2} - Score: {self.score1}"

    def ToDict(self) -> dict:
        return {
            "team1": self.team1,
            "team2": self.team2,
            "score1": self.score1,
            "score2": self.score2
        }