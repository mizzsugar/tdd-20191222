import enum
from typing import (
    Iterable,
    Optional
)
import random


class Card(enum.IntEnum):
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    J = 10
    Q = 10
    K = 10
    A = 11


def sum_point(cards: Iterable[Card]) -> int:
    """カードの合計値を算出します。
    """
    sorted_cards = sorted(cards)
    points = 0
    for card in sorted_cards:
        if not card == Card.A:
            points += card
            continue
        if points + card > 21:
            points += 1
        else:
            points += card
    return points


class Player:
    def __init__(self):
        self.is_stand = False
        self.cards = random.choices(list(Card), k=2)

    def hit(self) -> None:
        if self.is_stand:
            return
        self.cards.append(random.choice(list(Card)))

    def stand(self) -> None:
        self.is_stand = True


class Judge:
    def __init__(self, player: Player, dealer: Player) -> None:
        self.player = player
        self.dealer = dealer
    
    def tell_loser(self) -> Optional[Player]:
        if sum_point(self.player.cards) > 21:
            return self.player
        return None
