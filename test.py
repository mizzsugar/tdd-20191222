from card import Card


def test_数字をそのまま数える_2():
    card = Card.two
    assert card == 2


def test_数字をそのまま数える_J():
    card = Card.J
    assert card == 10
