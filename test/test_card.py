import unittest
from src.card import Card
from src.card_type import Card_type
from src.suit import Suit


class CardTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        pass

    def tearDown(self):  # this method will be run after each test
        pass

    def test_card_has_type(self):
        card = Card(Suit.CLUBS,None,Card_type.ACE)
        self.assertEqual(card.type, Card_type.ACE)

    def test_card_has_suit(self):
        card = Card(Suit.CLUBS,None,Card_type.ACE)
        self.assertEqual(card.suit, Suit.CLUBS)
    

    


if __name__ == '__main__':
    unittest.main()