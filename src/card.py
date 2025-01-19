from src.suit import Suit
class Card:
    def __init__(self,suit:int,value:int,type:int):
        self.suit = suit
        self.value = value
        self.type = type


    def __str__(self):
        return "%s of %s" %  (self.type, self.suit)
    

