from cards1 import Card
import random
suits_list = ["hearts", "diamonds", "spades", "clubs"]
values_list = ["A"]
unicode_symbols = {"hearts":u"\u2661", "diamonds":u"\u2662", "spades":u"\u2664", "clovers": "\u2667"}
# u"..." inside the paranthesis is unicode.
for num in range(2,11):
    values_list.append(str(num))
values_list.extend(["J", "Q", "K"]) # Note that you use extend and not append.

cards = []
for suit in suits_list:
    for values in values_list:
        c = Card(values, suit)
        if values == "A": 
            c.numvalues = [1,11] 
        elif values in ["J", "K", "Q"]:
            c.numvalues = [10]
        else:
            c.numvalues = [int(values)]
        cards.append(c)

def main():
    dealer_hand = []
    player_hand = []
    shuffleDeck(cards)
    for i in range(5):
        dealer_hand.append(random.choice(cards))
        player_hand.append(random.choice(cards))
    print(f"Here is the dealer's hand: {dealer_hand}.")
    print(f"Here is your hand: {player_hand}.")
    # print(cards, end=", ")

def shuffleDeck(cards):
    random.shuffle(cards)

main()
