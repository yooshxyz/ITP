# values
# suits
# numbers

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.numvalues = []

    def __repr__(self):
        symbols = {"hearts":u"\u2661", "diamonds":u"\u2662", "spades":u"\u2664", "clubs": "\u2667"}
        return self.value + symbols[self.suit]
