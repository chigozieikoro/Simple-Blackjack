class PlayerBank:
    def __init__(self,balance):
        self._balance = balance
        self._is_winner = False
        self._is_bust = False
        self._bets_placed = 0

    def pay_winner(self, amount):
        self._is_winner = True
        self._balance += amount

    def bust(self):
        self._is_winner = False
        self._is_bust = True

    def set_status(self,bool):
        self._is_winner = bool

    def check_status(self):
        return self._is_winner

    def is_bust(self):
        return self._is_bust

    def get_balance(self):
        return self._balance

    def get_wager(self):
        return self._bets_placed

    def enter_bet(self, wager):
        if wager > self._balance:
            raise RuntimeError('Your wager is greater than the balance')
        self._bets_placed = self._bets_placed + wager
        self._balance = self._balance - wager

    def __str__(self):
        wager = self.get_wager()
        buster = ""
        if self.check_status() == True:
            buster = "winner!"
        else:
            buster = "bust."
        s = "Player assets:\nbet %d balance %d %s" %(wager, self.get_balance(), buster)
        return s



