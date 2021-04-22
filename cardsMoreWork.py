from random import shuffle

unicode_symbols = {"hearts":u"\u2661", "diamonds":u"\u2662", "spades":u"\u2664", "clovers": "\u2667"}
Values = {2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"10", "J":10, "Q": 10, "k":10}
deck = {}
x = 2
while x < len(Values) - 3:
    deck[x] = Values[x]
    x += 1

print(deck)



