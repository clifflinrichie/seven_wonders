from src.generate_cards import generate_cards
from src.models.card import Card

card_list = generate_cards()

def test_generate_cards_exist():
    assert card_list

def test_cards_are_cards():
    assert all(isinstance(card, Card) for card in card_list)

def test_no_duplicate_card_names():
    assert len(card_list) == len({card.name for card in card_list})