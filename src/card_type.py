from enum import Enum

'''
Enumeration for card options
'''
class Card_type(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    def __str__(self):
        return self.name[0] + self.name[1:].lower()
