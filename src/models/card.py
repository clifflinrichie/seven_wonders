from src.constants.color import Color

class Card:
    def __init__(self, name: str, cost, age: int, color: Color, effects: list): 
        self.name = name
        self.cost = cost
        self.age = age
        self.color = color
        self.effects = effects
