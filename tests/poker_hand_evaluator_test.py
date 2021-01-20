import unittest

from poker_hand_evaluator import PokerHand


class PokerHandEvaluator(unittest.TestCase):
    def test_pairs(self):
        p1_hand = PokerHand("5H 5C 6S 7S KD")
        p2_hand = PokerHand("2C 3S 8S 8D TD")
        self.assertLess(p1_hand, p2_hand)

    def test_high_card(self):
        p1_hand = PokerHand("5D 8C 9S JS AC")
        p2_hand = PokerHand("2C 5C 7D 8S QH")
        self.assertGreater(p1_hand, p2_hand)

    def test_flush(self):
        p1_hand = PokerHand("2D 9C AS AH AC")
        p2_hand = PokerHand("3D 6D 7D TD QD")
        self.assertLess(p1_hand, p2_hand)

    def test_pair(self):
        p1_hand = PokerHand("4D 6S 9H QH QC")
        p2_hand = PokerHand("3D 6D 7H QD QS")
        self.assertGreater(p1_hand, p2_hand)

    def test_full_house(self):
        p1_hand = PokerHand("2H 2D 4C 4D 4S")
        p2_hand = PokerHand("3C 3D 3S 9S 9D")


if __name__ == "__main__":
    unittest.main()
