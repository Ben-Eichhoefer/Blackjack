from unittest.mock import patch
import unittest

from src.card import Card
from src.deck import Deck
from src.player import Player
from src.card_type import Card_type
from src.suit import Suit
from blackjack import Blackjack

'''
Tests to demonstrate the required scenarios
'''
class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.player = Player("Player_0")
        


    def tearDown(self):  # this method will be run after each test
        pass
    
    
    # Given I play a game of blackjack When I am dealt my opening hand Then I have two cards
    @patch('builtins.input', return_value='11')
    def test_deal(self,input):
        self.game = Blackjack()
        self.game.players = [self.player]
        self.game.deck.shuffle_deck()
        self.game.deal()
        self.assertEqual(len(self.player.hand),2)

    # Given I have a valid hand of cards When I choose to ‘hit’ Then I receive another card And my score is updated 
    @patch('builtins.input', return_value='11')
    def test_valid_hit(self,input,print):
        self.player.hand = [Card(Suit.CLUBS,5,Card_type.FIVE),Card(Suit.HEARTS,5,Card_type.FIVE)]
        self.player.score = 10
        card_val = self.game.deck.cards[-1].value
        score_old = 10
        score_new = self.player.hit(self.game.deck.hit())
        self.assertEqual(score_new, score_old+card_val)

    # Given my score is updated or evaluated When it is 21 or less Then I have a valid hand
    def test_valid_hit(self):
        self.player.hand = [Card(Suit.CLUBS,5,Card_type.FIVE),Card(Suit.HEARTS,5,Card_type.FIVE)]
        self.player.score = 10
        self.player.hit(Card(Suit.CLUBS,5,Card_type.SIX))
        self.assertTrue(self.player.inPlay)
    
    # Given I have a valid hand of cards When I choose to ‘stand’ Then I receive no further cards And my score is evaluated
    @patch('builtins.input', return_value='2')
    def test_stand(self,input):
        self.player.hand = [Card(Suit.DIAMONDS,10,Card_type.TEN),Card(Suit.HEARTS,10,Card_type.TEN)]
        self.player.score = 20
        choice = self.player.options()
        self.assertEqual(choice,2)
        self.assertFalse(self.player.inPlay)

    # Given my score is updated When it is 22 or more Then I am ‘bust’ and do not have a valid hand
    def test_invalid_hit(self):
        self.player.hand = [Card(Suit.DIAMONDS,10,Card_type.TEN),Card(Suit.HEARTS,5,Card_type.FIVE)]
        self.player.score = 15
        self.player.hit(Card(Suit.CLUBS,10,Card_type.TEN))
        self.assertFalse(self.player.inPlay)
    
    
    # Given I have a king and an ace When my score is evaluated Then my score is 21
    @patch('builtins.input', return_value='11')
    def test_dealt_blackjack_hand(self,input):
        self.player.hit(Card(Suit.CLUBS,10,Card_type.KING))
        self.player.hit(Card(Suit.CLUBS,11,Card_type.ACE))
        self.assertEqual(self.player.score,21)
    
    # Given I have a king, a queen, and an ace When my score is evaluated Then my score is 21
    def test_king_queen_ace(self):
        self.player.hit(Card(Suit.CLUBS,10,Card_type.KING))
        self.player.hit(Card(Suit.CLUBS,10,Card_type.QUEEN))
        self.player.hit(Card(Suit.CLUBS,11,Card_type.ACE))
        self.assertEqual(self.player.score,21)
    
    # Given I have a nine, a nine, and an ace When my score is evaluated Then my score is 21
    @patch('builtins.input', return_value='11')
    def test_nine_ace_ace(self,input):
        self.player.hit(Card(Suit.CLUBS,9,Card_type.NINE))
        self.player.hit(Card(Suit.HEARTS,11,Card_type.ACE))
        self.player.hit(Card(Suit.CLUBS,11,Card_type.ACE))
        self.assertEqual(self.player.score,21)

        
        
    '''
    Other constrains are best demonstrated via gameplay
    '''
        




if __name__ == '__main__':
    unittest.main()
