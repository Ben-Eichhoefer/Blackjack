from unittest.mock import patch
import unittest
from src.player import Player
from src.card import Card
from src.card_type import Card_type
from src.suit import Suit


class PlayerTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.player = Player("test")

    def tearDown(self):  # this method will be run after each test
        pass

    def test_hit_adds_card(self):
        card = Card(Suit.CLUBS,10,Card_type.TEN)
        self.player.hit(card)
        self.assertIs(card,self.player.hand[0])

    def test_hit_increases_score(self):
        card = Card(Suit.CLUBS,10,Card_type.TEN)
        self.player.hit(card)
        self.assertEqual(self.player.score, 10)

    def test_ace_auto_set_one(self):
        self.player.score = 20
        self.player.hand = [Card(Suit.CLUBS,10,Card_type.TEN),Card(Suit.DIAMONDS,10,Card_type.TEN)] 
        score = self.player.hit(Card(Suit.CLUBS,11,Card_type.ACE)) # add ace
        self.assertEqual(score,21)
    
    def test_change_ace_in_hand(self):
        self.player.hand=[Card(Suit.CLUBS,11,Card_type.ACE),Card(Suit.CLUBS,7,Card_type.SEVEN)]
        self.player.score = 18
        score = self.player.hit(Card(Suit.CLUBS,5,Card_type.FIVE))
        self.assertEqual(score,13)
        self.assertEqual(self.player.hand[0].value,1)

    @patch('builtins.input', return_value='11')
    def test_ace_choice_11(self,input):
        score = self.player.hit(Card(Suit.CLUBS,11,Card_type.ACE))
        self.assertEqual(score,11)
    
    @patch('builtins.input', return_value='1')
    def test_ace_choice_1(self,input):
        score = self.player.hit(Card(Suit.CLUBS,11,Card_type.ACE))
        self.assertEqual(score,1)

    @patch('builtins.input', return_value='11')
    def test_consecutive_aces(self,input):
        score = self.player.hit(Card(Suit.CLUBS,11,Card_type.ACE))
        self.assertEqual(score,11)
        score = self.player.hit(Card(Suit.CLUBS,11,Card_type.ACE))
        self.assertEqual(score,12)




if __name__ == '__main__':
    unittest.main()
