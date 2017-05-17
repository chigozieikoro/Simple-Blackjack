from hand import Hand
from player_bank import PlayerBank


class ConservativePlayer:

    def make_bet(self, bank):
        current_balance = bank.get_balance()
        if current_balance < 20:
            return 0


        if current_balance <= 40:
            return 10
        elif current_balance <= 60:
            return 20
        elif current_balance <= 80:
            return 30
        elif current_balance <= 100:
            return 35
        else:
            return 45






    def use_ace_hi(self, player_hand):
        if player_hand.has_ace() == True:
            score_ace_hi = player_hand.score_hand(True)
            if score_ace_hi <= 21:
                return True
            else:
                return False



    def want_card(self, player_hand, player_bank, dealer_hand, cards_dealt):
        player_score = player_hand.get_score()

        if player_bank.is_bust() == True:
            return False

        if player_score <= 10:
            return True

        elif player_score <= 15 and player_hand.has_ace() == False:
            return True

        elif player_score <= 17 and player_hand.has_ace() == True:
            return True
        elif player_score <= 17 and player_hand.has_ace():
            return False
        elif player_score <= 17 and player_hand.has_ace() == False:
            return True

        elif player_score >= 18 and player_hand.has_ace():
            return False
        elif player_score > 18:
            return False
        else:
            return False

    def __str__(self):
        s = "Conservative Player Strategy"
        return s








