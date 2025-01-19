from enum import Enum

'''
Enumeration for card suits
'''
class Suit(Enum):
    
    SPADE = 0
    CLUBS = 1 
    HEARTS = 2
    DIAMONDS = 3
    def __str__ (self):
        suits = {self.CLUBS:"\u2663",self.DIAMONDS:"\u2666",self.HEARTS:"\u2665",self.SPADE:"\u2660"}
        return(suits[self])
