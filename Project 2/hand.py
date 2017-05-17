
class Hand:

    def __init__(self):
        self._cards = []
        self._score = 0


    def add_card(self,card):
        self._cards.append(card)


    def get_score(self):
        return self._score


    def set_score(self, score):
        self._score = score


    def has_ace(self):
        for card in self._cards:
            list = card[0]
            rank = list[0]
            if rank == 'A':
                return True
        return False


    def score_hand(self,bool):
        score = 0
        for card in self._cards:
            card_list = card[0]
            """Face cards are worth 10"""
            if card_list == 'A':
                if bool == True:
                    score = score + 11
                else:
                    score = score + 1

            elif card_list == 'J' or card_list == 'Q' or card_list == 'K':
                score = score + 10
            else:
                score = score + int(card_list)
        return score


    def get_cards(self):
        new_list = list(self._cards)
        return new_list

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        list = self.get_cards()
        s = str(list).strip('[]')
        g = "score: %d\n" %(self.get_score())
        final_string = "%s%s" %(g, s)
        return final_string