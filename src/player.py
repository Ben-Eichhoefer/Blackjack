from src.card_type import Card_type

'''
Class representing a user player
'''
class Player:
    def __init__(self,name):
        self.hand=[]
        self.score = 0
        self.inPlay = True
        self.name=name

    # Present player with game options
    def options(self)->int:
        print(self.name+''' -  Please choose an action:
                1: Hit
                2: Stand
        ''')
        while True:
            try:
                choice = int(input("Choice: "))
                break
            except ValueError:
                print("Please enter an integer")

        if choice < 1:
            choice = 1
        if choice > 2:
            choice =2
        # Remove player from play
        if choice == 2:
            print("Stand! Your score: %s" % self.score)
            self.inPlay = False
        return choice

    # hit
    # TODO add method to re-assign high ace if win possible
    def hit(self,card)->int:
        # automatically assign ace value if bust or win
        # else let user choose ace value
        if card.type == Card_type.ACE and self.score + 11 > 21:
            card.value = 1
        elif card.type == Card_type.ACE and self.score + 11 == 21:
            card.value == 11
        elif card.type == Card_type.ACE:
            while True:
                try:
                    value = int(input(self.name+" - Please choose ace value (1 or 11): "))
                    if value == 1 or value == 11:
                        break
                    print("Please enter either 1 or 11")
                except ValueError:
                    print("Please enter an integer")
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
