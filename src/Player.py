from src.Gender import Gender
from src.Serialize import Serialize

class Player(Serialize):
    def __init__(self, name: str, player_id: int, gender:Gender):
        self.name = name
        self.player_id = player_id
        self.gender = gender

    def __eq__(self, value):
        if isinstance(value, Player):
            if self.player_id is not value.player_id:
                return False
            if self.gender is not value.gender:
                return False
            if self.name is not value.name:
                return False
        return True

    def GetGender(self) -> Gender:
        return self.gender
    def GetName(self) -> str:
        return self.name
    def GetId(self) -> int:
        return self.player_id

    def __str__(self):
        return f"Player {self.player_id}: {self.name}"
    
    def ToDict(self) -> dict:
        return {
            "name": self.name,
            "id":self.player_id,
            "gender": self.gender.value
        }