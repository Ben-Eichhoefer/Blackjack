from src.suit import Suit
from src.card_type import Card_type
'''
Class representing a playing card
'''
class Card:
    def __init__(self,suit:Suit,value:int,type:Card_type):
        self.suit = suit
        self.value = value
        self.type = type


    def __str__(self):
        return "%s of %s" %  (self.type, self.suit)
    

