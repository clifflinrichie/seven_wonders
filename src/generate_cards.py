from src.models.card import Card
from src.models.resource_bundle import ResourceBundle
from src.effects.resource_effect import ResourceEffect
from src.constants.color import Color


def generate_cards():
    all_cards = []
    lumber_yard = Card(name="lumber_yard", 
                       cost=0, 
                       age=1, 
                       color=Color.brown, 
                       effects=[ResourceEffect(ResourceBundle(wood=1))])

    all_cards.append(lumber_yard)
    return all_cards