import pytest

from src.generate_cards import generate_cards

def test_generate_cards():
    card_list = generate_cards()
    assert card_list