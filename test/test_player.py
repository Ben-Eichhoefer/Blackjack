from unittest.mock import patch
import unittest
from src.player import Player
from src.card import Card


class DeckTestCase(unittest.TestCase):

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




if __name__ == '__main__':
    unittest.main()
