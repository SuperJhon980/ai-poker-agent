from random import shuffle


class DeckOfCards:
    # Init creates a new deck
    def __init__(self):
        self.deck = []
        self.num_of_cards = 0
        self.new_deck(False)

    # Creates a new shuffled deck
    def new_deck(self, has_jokers):
        self.deck = [i for i in range(52)]
        self.num_of_cards = 52

        if has_jokers:
            self.deck.append(52)
            self.deck.append(53)
            self.num_of_cards += 2

        shuffle(self.deck)

    # Pops card and returns it. Returns None if empty
    def draw_card(self):
        if self.num_of_cards > 0:
            self.num_of_cards -= 1
            return self.deck.pop()

        print("Deck is empty, cannot draw a card")
        return None


def print_card(card):
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Two", "Three", "Four", "Five", "Six", "Seven",
        "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"
    ]

    if card == 52:
        print("Red Joker")
    elif card == 53:
        print("Black Joker")
    else:
        suit = SUITS[card // 13]
        rank = RANKS[card % 13]
        print(rank, "of", suit)


def test():
    my_deck = DeckOfCards()
    my_deck.new_deck(True)

    card = my_deck.draw_card()
    while card:
        print_card(card)
        card = my_deck.draw_card()


if __name__ == "__main__":
    test()
