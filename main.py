from timeit import default_timer as timer
from poker_hand_evaluator import PokerHand

if __name__ == "__main__":
    player_1_wins = 0
    player_1_rank_wins = 0
    total = 0
    start = timer()
    with open("data/poker.txt", "r") as f:
        for line in f.readlines():
            total += 1
            player_1_cards, player_2_cards = line[:15], line[15:]
            player_1_hand = PokerHand(player_1_cards)
            player_2_hand = PokerHand(player_2_cards)
            if player_1_hand > player_2_hand:
                player_1_wins += 1
    end = timer()
    print(f"Player 1 wins: {player_1_wins} | Time Elapsed: {(end-start)*1000:.0f}ms")
