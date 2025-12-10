from enum import Enum
from random import shuffle
from dataclasses import dataclass
class DeckOfCards():
    # Init Creates a new deck
    def __init__(self):
        self.deck = []
        self.numOfCards = 0
        self.newDeck(False)

    # Creates a new shuffled deck
    def newDeck(self, hasJokers):
        self.deck = []
        self.numOfCards = 52
        for card in Card:
            if card is not Card.JOKER:
                for suit in Suit:
                    if suit not in (Suit.RED, Suit.BLACK):
                        self.deck.append(PlayingCard(card, suit))

        if hasJokers:
            self.deck.append(PlayingCard(Card.JOKER, Suit.BLACK))
            self.deck.append(PlayingCard(Card.JOKER, Suit.RED))
            self.numOfCards += 2

        shuffle(self.deck)
        return
    
    # pops card and returns it. returns None if empty
    def drawCard(self):
        if self.numOfCards > 0:
            self.numOfCards -= 1
            return self.deck.pop()
        
        print("Deck is empty, cannot draw a card")
        return None
    
# Card enum. Ace-Joker
class Card(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    JOKER = 14

# Suit enum. Has Red and Black for jokers
class Suit(Enum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4
    RED = 5
    BLACK = 6

@dataclass
class PlayingCard:
    card: Card
    suit: Suit


def main():
    myDeck = DeckOfCards()
    card = myDeck.drawCard()
    while card:
        print(card.card.name, "of", card.suit.name)
        card = myDeck.drawCard()

main()