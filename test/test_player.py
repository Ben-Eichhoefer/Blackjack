from unittest.mock import patch
import unittest
from src.player import Player
from src.card import Card
from src.card_type import Card_type


class PlayerTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.player = Player("test")


    def tearDown(self):  # this method will be run after each test
        pass

    def test_hit_adds_card(self):
        card = Card(1,1,1)
        self.player.hit(card)
        self.assertIs(card,self.player.hand[0])

    def test_hit_increases_score(self):
        card = Card(1,10,10)
        self.player.hit(card)
        self.assertEqual(self.player.score, 10)

    def test_ace_auto_set_one(self):
        self.player.score = 20
        self.player.hand = [Card(1,10,10),Card(2,10,10)] 
        score = self.player.hit(Card(1,11,1)) # add ace
        self.assertEqual(score,21)
    
    def test_change_ace_in_hand(self):
        self.player.hand=[Card(1,11,Card_type.ACE),Card(1,7,Card_type.SEVEN)]
        self.player.score = 18
        score = self.player.hit(Card(1,5,Card_type.FIVE))
        self.assertEqual(score,13)
        self.assertEqual(self.player.hand[0].value,1)

    @patch('builtins.input', return_value='11')
    def test_ace_choice_11(self,input):
        score = self.player.hit(Card(1,11,Card_type.ACE))
        self.assertEqual(score,11)
    
    @patch('builtins.input', return_value='1')
    def test_ace_choice_1(self,input):
        score = self.player.hit(Card(1,11,Card_type.ACE))
        self.assertEqual(score,1)






if __name__ == '__main__':
    unittest.main()
