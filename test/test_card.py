import unittest
from src.card import Card
from src.card_type import card_type
from src.suit import suit


class CardTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        pass

    def tearDown(self):  # this method will be run after each test
        pass

    def test_card_has_type(self):
        card = Card(suit.CLUBS,None,card_type.ACE)
        self.assertEqual(card.type, card_type.ACE)

    def test_card_has_suit(self):
        card = Card(suit.CLUBS,None,card_type.ACE)
        self.assertEqual(card.suit, suit.CLUBS)
    

    


if __name__ == '__main__':
    unittest.main()