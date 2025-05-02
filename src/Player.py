from src.Gender import Gender

class Player:
    def __init__(self, name: str, player_id: int, gender:Gender):
        self.name = name
        self.player_id = player_id
        self.gender = gender

    def __str__(self):
        return f"Player {self.player_id}: {self.name}"