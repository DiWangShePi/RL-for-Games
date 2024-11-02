import random


class LiarsBar:
    def __init__(self):
        self.cards = [0 for _ in range(8)] + [1 for _ in range(12)]
        self.player1_cards = None
        self.player2_cards = None
        self.player3_cards = None
        self.player4_cards = None

        self.last_turn = None

    def reset(self):
        random.shuffle(self.cards)

        self.player1_cards = (5, 0, self.cards[:5].count(0), self.cards[:5].count(1))
        self.player2_cards = (5, 0, self.cards[5:10].count(0), self.cards[5:10].count(1))
        self.player3_cards = (5, 0, self.cards[10:15].count(0), self.cards[10:15].count(1))
        self.player4_cards = (5, 0, self.cards[15:].count(0), self.cards[15:].count(1))

        return self.player1_cards, self.player2_cards, self.player3_cards, self.player4_cards

    def step(self, player, action, action_args):
        # Call last player to be a liar
        if action == 0:
            if self.last_turn:
                return 100, True, None
            else:
                return -100, True, None

        # decided to play honest
        if action == 1:
            pass

        # decided to lie
        if action == 2:
            pass

    def get_player_state(self, player_number):
        return getattr(self, f"player{player_number}_cards")

