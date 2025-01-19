from src.deck import Deck
from src.player import Player

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.players=[]

    def play(self):
        num_players = int(input("Please select number of players(1-4)"))
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

                print("Hand: ",end="" )
                for i in p.hand:
                    print(i,end=" ")
                print("")
                choice = p.options()
                if choice == 1:
                    score = p.hit(self.deck.hit())
                    if score >21:
                        print("Bust!")
                        p.inPlay = False
                    # If player blackjack exit early
                    if score == 21:
                        print("Blackjack - Game Over\n" + p.name + " wins!")
                        break
                running = running or p.inPlay # if player still in play running becomes True
                    
        

    # Deal a card to each player
    # Return False if game ends
    def deal(self) -> bool:
        for p in self.players:
            p.hit(self.deck.hit())
        for p in self.players:
            score = p.hit(self.deck.hit())
            # If a player reaches 21 end game
            if score == 21:
                print("Blackjack - Game Over\n" + p.name + " wins!")
                return False
        return True
        

            
        



if __name__ == '__main__':
    game = Blackjack()
    game.play()
