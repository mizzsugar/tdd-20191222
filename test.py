from card import Card, Player, Judge
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


def test_プレイヤーにはカードが最初に2枚配られる():
    assert len(Player().cards) == 2


def test_プレイヤーがhitするとカードが1枚増える():
    player = Player()
    player.hit()
    assert len(player.cards) == 3


def test_スタンドを選択すると以降ゲーム終了まで何も出来ない():
    player = Player()
    assert len(player.cards) == 2

    player.stand()
    player.hit()
    assert len(player.cards) == 2


def test_プレイヤーのカード合計が21を超えるとプレイヤーの負け():
    player = Player()
    player.cards = [Card.J, Card.Q, Card.K]
    dealer = Player()
    judge = Judge(player, dealer)
    assert judge.tell_loser() == player


def test_プレイヤーのカードの合計値が21以下で負けない():
    player = Player()
    player.cards = [Card.J, Card.three, Card.two]
    dealer = Player()
    judge = Judge(player, dealer)
    assert judge.tell_loser() != player
