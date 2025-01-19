from src.suit import Suit
from src.card import Card
from src.card_type import Card_type

from random import shuffle
'''
Class representing a deck
'''
class Deck:
    def __init__(self):
        self.cards = []

    def shuffle_deck(self):
        for i in Suit:
            for j in Card_type:
                if j.value < 10:
                    self.cards.append(Card(i,j.value,j))
                else:
                    self.cards.append(Card(i,10,j))
        shuffle(self.cards)

    def hit(self):
        # pop from self.cards
        return self.cards.pop()
