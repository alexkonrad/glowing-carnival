from enum import IntEnum, auto


class PokerHandRank(IntEnum):
    """
    Poker hand strengths ranked in ascending order.
    """

    HighCard = auto()
    OnePair = auto()
    TwoPairs = auto()
    ThreeOfAKind = auto()
    Straight = auto()
    Flush = auto()
    FullHouse = auto()
    FourOfAKind = auto()
    StraightFlush = auto()
    RoyalFlush = auto()
