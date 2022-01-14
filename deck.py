import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle()


    def create_deck(self):
        for suit in Card.SUIT_SYMBOLS:
            for value in Card.VALUE_NAMES:
                new_card = Card(suit, value)
                self.cards.append(new_card)


    def shuffle(self):
        random.shuffle(self.cards)


    def deal(self, num_cards):
        dealt_cards = []

        for _ in range(num_cards):
            top_card = self.cards.pop()
            dealt_cards.append(top_card)

        return dealt_cards
