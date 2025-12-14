# Validates string is an integer and prompts for one if not
def verify_int(in_string):
    my_int = in_string
    while not my_int.isdigit():
        my_int = input("Input is not a digit. Try again:\n")
    return int(my_int)


# Returns string from the int representation of the card
def get_card(card):
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Two", "Three", "Four", "Five", "Six", "Seven",
        "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"
    ]

    if card == 52:
        return "Red Joker"
    elif card == 53:
        return "Black Joker"
    else:
        suit = SUITS[get_suit(card)]
        rank = RANKS[get_rank(card)]
        return rank + " of " + suit

# Abstracted away the math so code looks cleaner
def get_suit(card):
    return card // 13


def get_rank(card):
    return card % 13