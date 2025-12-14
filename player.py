# Class for poker Player. Small class
class Player:
    def __init__(self, cash):
        self.cash = cash
        self.hand = []
        self.current_bet = 0