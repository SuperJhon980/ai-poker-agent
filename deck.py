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
        self.deck = [i for i in range(52)]
        self.numOfCards = 52

        if hasJokers:
            self.deck.append(52)
            self.deck.append(53)
            self.numOfCards += 2

        #shuffle(self.deck)
        print(self.deck)
        return
    
    # pops card and returns it. returns None if empty
    def drawCard(self):
        if self.numOfCards > 0:
            self.numOfCards -= 1
            return self.deck.pop()
        
        print("Deck is empty, cannot draw a card")
        return None
    

def printCard(card):
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

    if(card == 52):
        print("Red Joker")
    elif(card == 53):
        print("Black Joker")
    else:
        suit = SUITS[card // 13]
        rank = RANKS[card % 13]
        print(rank, "of", suit)

    


def main():
    myDeck = DeckOfCards()
    myDeck.newDeck(True)
    card = myDeck.drawCard()
    while card:
        card = myDeck.drawCard()
        printCard(card)
        


main()