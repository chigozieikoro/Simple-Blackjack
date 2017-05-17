import random

class RandomPlayer:

    def make_bet(self,bank):
        current_balance = bank.get_balance()
        if current_balance != 0:
            wager = random.randint(0,current_balance)
            return wager
        else:
            return 0


    def use_ace_hi(self, player_hand):
        """work on hand_copy so we can get the theoretical score without altering the dealer"""
        """if the random player's high score is good enough to use, he may still not use it!"""
        if player_hand.has_ace() == True:
            score_ace_hi = player_hand.score_hand(True)
            score_ace_low = player_hand.score_hand(False)
            if score_ace_hi <= 21:
                wager = random.randint(0,1)
                if wager == 0:
                    return True
                else:
                    return False
            else:
                return False



    def want_card(self, player_hand, player_bank, dealer_hand, cards_dealt):
        """a smart player would take the information given and make an educated decision about whether to take a card or not"""
        """a random player will just ask for a card without any inkling of strategy"""

        wager = random.randint(0,1)
        return wager == 1

    def __str__(self):
        s = "Random Player Strategy"
        return s


