from src.deck import Deck
from src.player import Player

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.players=[]

    def play(self):
        while True:
            try:
                num_players = int(input("Please select number of players(1-4)"))
                break
            except ValueError:
                print("Please enter an integer")
        if num_players < 1:
            num_players = 1
        if num_players > 4:
            num_players = 4
        
        self.deck.shuffle_deck()
        self.players=[Player("Player_"+str(i)) for i in range(0,num_players)]
        running = self.deal()

        if not running:
            return # exit game
        
        # Gameplay loop
        while running:
            running = False
            for p in self.players:
                print("\n=========== " + p.name + "'s turn ===========\n")
                if not p.inPlay:
                    if score < 21:
                        print(p.name," - Score =",p.score)
                    else:
                        print(p.name," is Bust")
                    continue

                print("Hand: ",end="| " )
                for i in p.hand:
                    print(i,end=" | ")
                print("")
                choice = p.options()
                if choice == 1:
                    card = self.deck.hit()
                    print(p.name," - drew",card)
                    score = p.hit(card)
                    
                    # If player blackjack exit early
                    if score == 21:
                        print("Blackjack - Game Over\n" + p.name + " wins!")
                        return
                running = running or p.inPlay # if player still in play running becomes True
        highest = Player(False)
        highest.score = 0
        for p in self.players:
            if p.score <= 21 and p.score > highest.score:
                highest = p
        if highest.name:
            print(highest.name," wins!\nWith a score of:", highest.score)
        else:
            print("Everyone bust, house wins")
            
            

                    
        

    # Deal a card to each player
    # Return False if game ends
    def deal(self) -> bool:
        for p in self.players:
            card = self.deck.hit()
            print(p.name,"receives",card)
            p.hit(card)
        for p in self.players:
            card = self.deck.hit()
            print(p.name,"receives",card)
            score = p.hit(card)
            # If a player reaches 21 end game
            if score == 21:
                print("Blackjack - Game Over\n" + p.name + " wins!")
                return False
        return True
        

            
        



if __name__ == '__main__':
    game = Blackjack()
    game.play()
