from src.Serialize import Serialize
from datetime import datetime

class Date(Serialize):
    def __init__(self, day: str = "", date: str = None, time: str = ""):
        self.day = day
        self.date:datetime = datetime.strptime(date, "%d-%m-%Y")
        self.time = time

    def GetDate(self) -> datetime:
        return self.date
    def GetDay(self) -> str:
        return self.day
    def GetTime(self) -> str:
        return self.time
    
    def __str__(self) -> str:
        return f"{self.day} {self.date.strftime('%d-%m-%Y')} om {self.time}"
    
    def ToDict(self) -> dict:
        return {
            "day": self.day,
            "date": self.date.strftime("%d-%m-%Y"),
            "time": self.time.strftime("%H:%M")
        }
