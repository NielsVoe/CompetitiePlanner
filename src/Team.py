from src.Player import Player

class Team:
    def __init__(self, name: str, id: str):
        self.id = id
        self.name = name
        self.players:list[Player] = []

    def AddPlayer(self, player: Player) -> bool:
        if player in self.players:
            return False
        self.players.append(player)
        return True

    def __str__(self) -> str:
        return f"Team {self.name} with members: {', '.join(self.players)}"