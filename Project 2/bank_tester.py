import unittest
from french_deck import FrenchDeck
from player_bank import PlayerBank
from hand import Hand
from conservative_player import ConservativePlayer
from random_player import RandomPlayer
from dealer import Dealer


class MyTestCase(unittest.TestCase):


    def test_game_start(self):
        dealer = Dealer(FrenchDeck(858))
        dealer.add_player("Chigozie", RandomPlayer(), PlayerBank(100))
        dealer.add_player("Jeff",ConservativePlayer(),PlayerBank(100))
        dealer.add_player("Chuck", RandomPlayer(), PlayerBank(100))
        dealer.deal_initial_hand()
        dealer.deal_dealer_hand()
        ' dealer.deal_player_hands()'
        dealer_hand = dealer.show_dealer_hand()
        dealer.deal_player_hands()
        dealer.take_bets()
        "self.assertTrue(dealer_hand.has_ace())"
        ''' print(dealer)'''
        dealer.settle_bets()

       # print(dealer)


    def test_take_bets(self):
        dealer = Dealer(FrenchDeck(123456))
        Bank1 = PlayerBank(100)
        Bank2 = PlayerBank(100)
        Bank3 = PlayerBank(100)
        dealer.add_player("Chigozie", RandomPlayer(), Bank1)
        dealer.add_player("Jeff", ConservativePlayer(), Bank2)
        dealer.add_player("Chuck", RandomPlayer(), Bank3)
        dealer.deal_initial_hand()
        dealer.deal_dealer_hand()
        dealer.deal_player_hands()
        dealer.take_bets()
        '''print(Bank1.get_wager())
        print(Bank2.get_wager())
        print(Bank3.get_wager())
        print("\n")'''
        dealer.take_bets()
        '''print(Bank1.get_wager())
        print(Bank2.get_wager())
        print(Bank3.get_wager())'''



    def test_deal_initial_hand(self):
        dealer = Dealer(FrenchDeck(1234456))
        Bank1 = PlayerBank(100)
        Bank2 = PlayerBank(100)
        Bank3 = PlayerBank(100)
        dealer.add_player("Chigozie", RandomPlayer(), Bank1)
        dealer.add_player("Pat", ConservativePlayer(), Bank2)
        dealer.add_player("Chuck", RandomPlayer(), Bank3)
        dealer.deal_initial_hand()



    def test_deal_cards(self):
        dealer = Dealer(FrenchDeck(66666652))
        dealer.add_player("Chigozie", RandomPlayer(), PlayerBank(100))
        dealer.add_player("Jeff",ConservativePlayer(),PlayerBank(100))
        dealer.add_player("Chuck", RandomPlayer(), PlayerBank(100))
        dealer.deal_initial_hand()
        dealer.deal_dealer_hand()
        dealer.deal_player_hands()
        dealer.deal_player_hands()
        dealer.take_bets()
        dealer.settle_bets()
        print(dealer)
        dealer.deal_player_hands()
        dealer.deal_dealer_hand()
        dealer.settle_bets()
        print("\n\n\n")
        print(dealer)






if __name__ == '__main__':
    unittest.main()
