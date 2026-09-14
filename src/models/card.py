from src.constants.color import Color
from collections import Counter

class Card:
    def __init__(self, name: str, cost, age: int, color: Color, effects: list, quantity_by_player_count: Counter): 
        self.name = name
        self.cost = cost
        self.age = age
        self.color = color
        self.effects = effects
        self.quantity_by_player_count = quantity_by_player_count
