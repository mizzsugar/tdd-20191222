from card import Card
import card


def test_数字をそのまま数える_2():
    card = Card.two
    assert card == 2


def test_数字をそのまま数える_J():
    card = Card.J
    assert card == 10


def test_複数枚の合計値を数える():
    assert Card.two + Card.J == 12


def test_複数枚の合計値を数える_絵札のみ():
    assert Card.J + Card.Q == 20


def test_Aは1か11として数える():
    assert Card.A == 11
    assert card.sum_point([Card.two, Card.three, Card.A]) == 16


def test_Aは1として数える():
    assert Card.A == 11
    assert card.sum_point([Card.J, Card.nine, Card.A]) == 20


def test_全てAである場合14になる():
    assert card.sum_point([Card.A, Card.A, Card.A, Card.A]) == 14