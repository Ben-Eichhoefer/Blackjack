from src.card_type import Card_type

class Player:
    def __init__(self,name):
        self.hand=[]
        self.score = 0
        #self.hole = hole
        self.inPlay = True
        self.name=name

    # Present player with game options
    def options(self)->int:
        choice = int(input(self.name+''' -  Please choose an action:
                1: Hit
                2: Stand
        '''))
        if choice == 2:    
            self.inPlay = False
        return choice

    # hit
    def hit(self,card)->int:
        if card.type == Card_type.ACE and self.score + 11 > 21:
            print(self.name+": Choosing an ace value of 11 will cause a bust")
        if card.type == Card_type.ACE:
            value = int(input(self.name+" - Please choose ace value (1 or 11): "))
            card.value = value
        self.score += card.value
        self.hand.append(card)
        return self.score
