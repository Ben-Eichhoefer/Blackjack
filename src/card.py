from src.suit import Suit
class Card:
    suits = {Suit.CLUBS:"\u2663",Suit.DIAMONDS:"\u2666",Suit.HEARTS:"\u2665",Suit.SPADE:"\u2660"}
    def __init__(self,suit,value,type):
        self.suit = suit
        self.value = value
        self.type = type


    def __str__(self):
        return "%s %s" %  (self.type, self.suits[self.suit])
    

