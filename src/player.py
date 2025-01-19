from src.card_type import Card_type

class Player:
    def __init__(self):
        self.hand=[]
        self.score = 0
        #self.hole = hole
        self.inPlay = True

    # Present player with game options
    def options(self)->int:
        pass

    # hit
    def hit(self,card):
        if card.type == Card_type.ACE and self.score + 11 > 21:
            print("Choosing an ace value of 11 will cause a bust")
        if card.type == Card_type.ACE:
            value = int(input("Please choose ace value (1 or 11)"))
            card.value = value
        self.score += card.value
        self.hand.append(card)
        
