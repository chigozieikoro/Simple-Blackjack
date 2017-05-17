from french_deck import FrenchDeck
from player_bank import PlayerBank
from hand import Hand
from copy import deepcopy
from dealer_player import DealerPlayer

class Dealer:
    def __init__(self, deck):
        self._deck = deck
        self._dealer = DealerPlayer()
        self._players = {}
        self.cards_dealt = []
        self._dealer_hand = Hand()

    def show_dealer_hand(self):
        return self._dealer_hand

    def add_player(self, handle, player, bank):
        hand = Hand()
        if handle in self._players:
            raise RuntimeError('Key already present in data')
        list = []
        list.append(hand)
        list.append(player)
        list.append(bank)
        self._players[handle] = list


    def take_bets(self):
        """order is hand, player, bank"""
        for key,value in self._players.items():
            current_player = value[1]
            player_bank = value[2]
            bank_copy = deepcopy(player_bank)
            wager = current_player.make_bet(bank_copy)
            player_bank.enter_bet(wager)
            value[1] = current_player
            value[2] = player_bank


    def deal_initial_hand(self):
        for key,value in self._players.items():
            card1 = self._deck.remove_card()
            card2 = self._deck.remove_card()
            player_hand = value[0]
            player_hand.add_card(card1)
            player_hand.add_card(card2)
            self.cards_dealt.append(card1)
            self.cards_dealt.append(card2)
            value[0] = player_hand
        dealer_card1 = self._deck.remove_card()
        dealer_card2 = self._deck.remove_card()
        self._dealer_hand.add_card(dealer_card1)
        self._dealer_hand.add_card(dealer_card2)
        self.cards_dealt.append(dealer_card1)


    def deal_player_hands(self):
        """order is hand, player, bank"""
        for key,value in self._players.items():
            current_player = value[1]
            current_bank = value[2]
            current_hand = value[0]
            score = current_hand.score_hand(current_player.use_ace_hi(deepcopy(current_hand)))
            current_hand.set_score(score)
            while current_player.want_card(deepcopy(current_hand), deepcopy(current_bank), deepcopy(self._dealer_hand), deepcopy(self.cards_dealt)) == True:
                add_card = self._deck.remove_card()
                current_hand.add_card(add_card)
                self.cards_dealt.append(add_card)
                score = current_hand.score_hand(current_player.use_ace_hi(deepcopy(current_hand)))
                current_hand.set_score(score)
                if score > 21:
                    break
            value[0] = current_hand
            value[1] = current_player
            value[2] = current_bank


    def deal_dealer_hand(self):
        boole = True
        dealer_score = self._dealer_hand.get_score()
        while dealer_score < 17 or dealer_score > 21:
            if dealer_score > 21 and boole == False:
                break
            if dealer_score > 21:
                boole = False
                break
            new_card = self._deck.remove_card()
            self._dealer_hand.add_card(new_card)
            self.cards_dealt.append(new_card)
            dealer_score = self._dealer_hand.score_hand(boole)
        self._dealer_hand.set_score(dealer_score)


    def settle_bets(self):
        for key,value in self._players.items():
            player_hand = value[0]
            player = value[1]
            player_bank = value[2]
            player_score = player_hand.get_score()
            dealer_score = self._dealer_hand.get_score()
            wager = player_bank.get_wager()
            if player_score > 21 or player_score == dealer_score:
                player_bank.bust()
            elif player_score <= 21:
                if player_score > dealer_score or dealer_score > 21:
                    player_bank.pay_winner(wager*2)
                else:
                    player_bank.bust()
            value[0] = player_hand
            value[1] = player
            value[2] = player_bank


    def __str__(self):
        s = "$$$$$$   Game Summary   $$$$$$\nDealer: \n"
        dealer_cards = str(self._dealer_hand)
        spaces = "\n\n"
        s += dealer_cards
        s += spaces

        for key, value in self._players.items():
            player_hand = value[0]
            player = value[1]
            player_bank = value[2]
            'player_hand.set_score(player_hand.score_hand(player.use_ace_hi(player_hand)))'
            file = "Player: %s\n%s\n%s\n" %(key, str(player_hand), str(player_bank))
            s += file
            s+= spaces
            value[0] = player_hand
            value[1] = player
            value[2] = player_bank
        return s






























        
