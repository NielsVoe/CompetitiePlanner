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
    
    def AddPlayers(self, players: list[Player]) -> bool:
        '''Add multiple players to the team.
        Returns True if all players were added, False if some were already present.'''
        allPlayersAdded = True
        for player in players:
            if player.name not in [p.name for p in self.players]:
                self.players.append(player)
            else:
                allPlayersAdded = False
        return allPlayersAdded

    def AddMatch(self, match: Teammatch) -> bool:
        if match in self.matches:
            return False
        self.matches.append(match)
        return True
    
    def AddMatches(self, matches: list[Teammatch]) -> bool:
        '''Add multiple matches to the team.
        Returns True if all matches were added, False if some were already present.'''
        allMatchesAdded = True
        for match in matches:
            if match.date not in [m.date for m in self.matches]:
                self.matches.append(match)
            else:
                allMatchesAdded = False
        # Make sure matches are sorted by date
        self.matches.sort(key=lambda m: m.date.date)
        return allMatchesAdded
    
    def GetMatches(self) -> list[Teammatch]:
        return self.matches
    
    def GetPlayers(self) -> list[Player]:
        return self.players

    def __str__(self) -> str:
        return f"Team {self.name} with members: {', '.join(str(player) for player in self.players)}"
    
    def ToDict(self) -> dict:
        return {
            "name": self.name,
            "id": self.id,
            "players": [player.ToDict() for player in self.players],
            "matches": [match.ToDict() for match in self.matches]
        }