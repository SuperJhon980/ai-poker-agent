from deck import DeckOfCards
from player import Player
import poker_utils as pu

class Poker:
    def __init__(self, num_of_players):
        self.players = []
        for _ in range(num_of_players):
            self.players.append(Player(1000))

        self.player_set = set(self.players)
        self.deck = DeckOfCards()
        self.cards = []
        self.folded = set()
        self.called = set()
        self.all_in = set()
        self.pot = 0
        self.bet = 2
        self.small_blind = 1
        self.big_blind = 2

    # deal_hands deals out cards to each player
    def deal_hands(self):
        dealer = self.players.pop(0)    # Rotate the dealer to back
        self.players.append(dealer)

        # get small and big blinds
        # small blind is first in list, big is second in list
        self.players[0].cash -= self.small_blind
        self.players[0].current_bet = self.small_blind
        self.players[1].cash -= self.big_blind
        self.players[1].current_bet = self.big_blind
        self.pot += self.big_blind + self.small_blind

        # deal hands
        for _ in range(2):
            for player in self.players:
                player.hand.append(self.deck.draw_card())

    # burn then deal n cards. Likely always 1 or 3
    def deal_cards(self, n):
        self.deck.draw_card()    # Burn a card
        for _ in range(n):
            self.cards.append(self.deck.draw_card())

    # get_bets goes around the table until the pot is good
    # (all bets are called or folded)
    def get_bets(self):
        actions = [self.fold, self.call, self.raise_bet]
        current_player = 2      # player that bets after big blind
        self.called = set()     # clear the called set

        # while everyone has either not called or folded
        while not self.player_set.issubset(self.folded.union(self.called.union(self.all_in))):

            # check for betting ability
            if len(self.player_set) - 1 == (len(self.folded)):
                print("Betting is done. No one can bet more")
                break

            # set current_player pointer back to beginning of players list
            if (current_player) >= len(self.players) - 1:
                current_player = 0
            else:
                current_player += 1

            player = self.players[current_player]

            # get player action
            if player not in self.folded and player not in self.called and player not in self.all_in:
                print(f"Player {current_player + 1}'s turn")
                action = pu.verify_int(input("Choose:\n1. Fold\n2. Check\n3. Raise\n"))
                actions[action - 1](player)

        # clear all the current bets in preparation for next round
        for player in self.players:
            player.current_bet = 0
        self.bet = 0

    # player can no longer bet
    def fold(self, player):
        self.folded.add(player)
        if player in self.called:
            self.called.remove(player)

    # player calls the current bet
    def call(self, player):
        # puts up the money needed to match the table's bet
        cash_to_call = self.bet - player.current_bet
        
        # TODO Gotta create secondary pot when bozo decides to all in when hes down...
        if(cash_to_call >= player.cash): # All in
            self.pot += player.cash
            player.cash = 0
            self.all_in.add(player)
            return

        player.cash -= cash_to_call
        self.pot += cash_to_call
        player.current_bet += cash_to_call
        self.called.add(player)

    # player raises the current bet by given input amount
    def raise_bet(self, player):
        # force to call if raising would be more money than possible
        if self.bet >= player.cash:
            self.call(player)
            print("Could not raise because current bet was greater than player cash")
            print(f"Called for {self.bet} instead")
            return
        
        new_bet = pu.verify_int(input("How much do you want to raise?\n"))
        # TODO input validation for int & legal bet of amount
        while(new_bet > player.cash):
            new_bet = pu.verify_int(input(f"You can raise max of {player.cash}\n"))
        
        self.bet += new_bet
        cash_to_call = self.bet - player.current_bet
        player.cash -= cash_to_call
        self.pot += cash_to_call
        player.current_bet += cash_to_call
        if player.cash == 0:
            self.all_in.add(player)
            self.called = set()
        else:
            self.called = {player}

    
    # Prints the current board state
    def print_board(self):
        print("--------")
        print("Community pile:")

        community_cards = ""
        for card in self.cards:
            community_cards += pu.get_card(card) + ", "
        print(community_cards[:-2])

        print(f"Total in Pot: {self.pot}")

        for i, player in enumerate(self.players):
            print(f"Player {i + 1}: {player.cash}")

            player_cards = ""
            for hand in player.hand:
                player_cards += pu.get_card(hand) + ", "

            print(player_cards[:-2])
        print("--------")

def main():
    num_of_players = pu.verify_int(input("How many players?\n"))
    my_poker_game = Poker(num_of_players)

    my_poker_game.deal_hands()
    my_poker_game.print_board()
    my_poker_game.get_bets()

    my_poker_game.deal_cards(3)
    my_poker_game.print_board()
    my_poker_game.get_bets()

    my_poker_game.deal_cards(1)
    my_poker_game.print_board()
    my_poker_game.get_bets()

    my_poker_game.deal_cards(1)
    my_poker_game.print_board()
    my_poker_game.get_bets()

    my_poker_game.print_board()


if __name__ == "__main__":
    main()
