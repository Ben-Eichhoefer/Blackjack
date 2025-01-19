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
        print(self.name+''' -  Please choose an action:
                1: Hit
                2: Stand
        ''')
        choice = int(input("Choice: "))
        if choice == 2:
            print("Stand! Your score: %s" % self.score)
            self.inPlay = False
        return choice

    # hit
    def hit(self,card)->int:
        if card.type == Card_type.ACE and self.score + 11 > 21:
            card.value = 1
        elif card.type == Card_type.ACE:
            value = int(input(self.name+" - Please choose ace value (1 or 11): "))
            card.value = value
        self.score += card.value
        self.hand.append(card)
        p=0
        while(self.score >21 and p < len(self.hand)):
            if self.hand[p].value == 11:
                self.score -= 10
                self.hand[p].value = 1
            p+=1
        if self.score > 21:
            self.inPlay = False
            print("Bust!")
        return self.score
