import unittest
from src.deck import Deck
from src.card import Card
from src.card_type import Card_type
from src.suit import Suit


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()
        self.deck.shuffle_deck()

    def tearDown(self):  # this method will be run after each test
        pass

    def test_number_of_cards(self):  # any method beginning with 'test_' will be run by unittest
        
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)

    def test_hit_returns_card(self):
        card = self.deck.cards[-1]
        hit = self.deck.hit()
        self.assertIs(card,hit)
    
    def test_hit_removes(self):
        len_deck_before = len(self.deck.cards)
        _ = self.deck.hit()
        self.assertLess(len(self.deck.cards),len_deck_before)
    
    # Test each card type appears once 
    def test_deck_unique(self):
        seen = set()
        for i in self.deck.cards:
            self.assertFalse((i.suit,i.type) in seen, "Violated card uniqueness")
            seen.add((i.suit,i.type))
        




if __name__ == '__main__':
    unittest.main()
