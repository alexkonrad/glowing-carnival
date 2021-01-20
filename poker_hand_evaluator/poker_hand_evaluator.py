from collections import Counter, defaultdict
from typing import List, Tuple, ValuesView

from .poker_hand_rank import PokerHandRank


class PokerHand:
    """
    Usage:
    >>> ph = PokerHand("5C TH TS JD 2D")
    >>> ph
    5C TH TS JD 2D | OnePair
    >>> ph.one_pair
    True
    >>> ph.flush
    False
    >>> ph2 = PokerHand("4H 3D 2S 8C 9C")
    >>> ph2
    4H 3D 2S 8C 9C | HighCard
    >>> ph > ph2
    True
    """

    SUITS = {"C", "S", "D", "H"}
    RANKS = defaultdict(
        int,
        {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "T": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        },
    )

    def __init__(self, cards: str):
        self.cards = cards
        self.ranks = Counter()
        self.suits = Counter()

        # Add card ranks and suits to multi-sets
        for char in cards:
            rank = PokerHand.RANKS[char]
            if rank in range(2, 15):
                self.ranks[rank] += 1
            elif char in PokerHand.SUITS:
                self.suits[char] += 1

    def __repr__(self):
        return f"{self.cards.strip()} | {next(x.name for x in PokerHandRank if x == self.rank)}"

    def __gt__(self, other):
        return (self.rank, self.sorted_ranks) > (other.rank, other.sorted_ranks)

    def __lt__(self, other):
        return (self.rank, self.sorted_ranks) < (other.rank, other.sorted_ranks)

    @property
    def rank(self) -> PokerHandRank:
        """
        The rank of a hand, given the cards.
        """
        if all((self.straight, self.flush, "A" in self.ranks)):
            return PokerHandRank.RoyalFlush
        if self.straight and self.flush:
            return PokerHandRank.StraightFlush
        if self.four_kind:
            return PokerHandRank.FourOfAKind
        if self.full_house:
            return PokerHandRank.FullHouse
        if self.flush:
            return PokerHandRank.Flush
        if self.straight:
            return PokerHandRank.Straight
        if self.three_kind:
            return PokerHandRank.ThreeOfAKind
        if self.two_pairs:
            return PokerHandRank.TwoPairs
        if self.one_pair:
            return PokerHandRank.OnePair
        return PokerHandRank.HighCard

    @property
    def rank_freqs(self) -> ValuesView:
        return self.ranks.values()

    @property
    def sorted_ranks(self) -> List[Tuple[int, int]]:
        """
        Card-frequencies and cards sorted descending by frequency and by rank.
        If two players have same-ranked hands, then the rank made up of the
        highest value wins. But if the ranks tie, then highest card wins.
        """
        return sorted(self.ranks, key=lambda card: (self.ranks[card], card))[::-1]

    @property
    def flush(self) -> bool:
        """
        All card suits are the same.
        """
        return len(self.suits.keys()) == 1

    @property
    def straight(self) -> bool:
        """
        All card ranks are consecutive.
        """
        ranks = sorted(self.ranks.keys())
        lo = int(ranks[0])
        straight = list(range(lo, lo + 5))
        return ranks == straight

    @property
    def four_kind(self) -> bool:
        """
        Four same-rank cards.
        """
        return 4 in self.rank_freqs

    @property
    def full_house(self) -> bool:
        """
        Three same-rank cards and two-same rank cards (of different rank).
        """
        return 2 in self.rank_freqs and 3 in self.rank_freqs

    @property
    def three_kind(self) -> bool:
        """
        Three same-rank cards.
        """
        return 3 in self.rank_freqs

    @property
    def two_pairs(self) -> bool:
        """
        Two pairs of same-rank cards.
        """
        return len([val for val in self.rank_freqs if val == 2]) == 2

    @property
    def one_pair(self) -> bool:
        """
        One pair of cards of the same rank.
        """
        return any(val for val in self.rank_freqs if val > 1)
