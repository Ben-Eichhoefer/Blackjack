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
        pass
        
