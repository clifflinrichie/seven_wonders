class Player:
    def __init__(self, name: str):
        self.name = name
        self.left_player = None
        self.right_player = None
        self.coins = 3
        self.points = 0
        self.cards_owned = []