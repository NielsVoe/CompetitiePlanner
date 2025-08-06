from src.Player import Player
from src.Teammatch import Teammatch
from src.Serialize import Serialize

class Team(Serialize):
    def __init__(self, name: str, id: str):
        self.id = id
        self.name = name
        self.players:list[Player] = []
        self.matches:list[Teammatch] = []

    def AddPlayer(self, player: Player) -> bool:
        if player in self.players:
            return False
        self.players.append(player)
        return True
    
    def AddMatch(self, match: Teammatch) -> bool:
        if match in self.matches:
            return False
        self.matches.append(match)
        return True
    
    def GetMatches(self) -> list[Teammatch]:
        return self.matches
    
    def GetPlayers(self) -> list[Player]:
        return self.players

    def __str__(self) -> str:
        return f"Team {self.name} with members: {', '.join(self.players)}"
    
    def ToDict(self) -> dict:
        return {
            "name": self.name,
            "id": self.id,
            "players": [player.ToDict() for player in self.players],
            "matches": [match.ToDict() for match in self.matches]
        }