class DealerPlayer:


    def make_bet(self, bank):
        """dealer will never make a bet"""
        return 0


    def use_ace_hi(self, player_hand):
        """I don't use this method for the dealer. In my code, the dealer is only scored in the deal_dealer_hand method"""
        score = player_hand.get_score()
        if score < 21:
            return True
        else:
            return False


    def want_card(self, player_hand, player_bank, dealer_hand, cards_dealt):
        dealer_score = player_hand.get_score()
        if dealer_score < 17 or dealer_score > 21:
            return True

        return False

    def __str__(self):
        s = "Dealer Player Strategy"
        return s