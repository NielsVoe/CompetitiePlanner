from src.Gender import Gender
from src.Serialize import Serialize

class Player(Serialize):
    def __init__(self, name: str, player_id: int, gender:Gender):
        self.name = name
        self.player_id = player_id
        self.gender = gender

    def __str__(self):
        return f"Player {self.player_id}: {self.name}"
    
    def ToDict(self) -> dict:
        return {
            "name": self.name,
            "id":self.player_id,
            "gender": self.gender.value
        }