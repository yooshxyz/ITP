from cards1 import Card
import random
from threading import Timer

def main():
    chips_value = random.randint(20,100)
    chips = f"{chips_value} chips"
    print(f"Before you start you need chips! You currently have {chips}.\n Please note that your amount of chips in the beginning is randomly chosen.\n If you wish to get more chips, then you must bet!")
    print(Card)
def cardAdd(values, values_list, suit, suits_list):
     gen_card = []
     for suit in suits_list:
            for values in values_list:
                c = Card(values, suit)
                gen_card.append(c)

def blackjack(chips, Card, gen_card):
    print("Welcome to blackjack! There will be a 10 second window in which you are able to 'hit' or 'stand' ")
    print("If at anytime you want to leave just type X and enter. The game will automatically stop if you run out of chips.") 
    suits_list = ["hearts", "diamonds", "spades", "clubs"]
    values_list = {"A":1 or 11, "Q": 10, "J": 10, "K": 10}
    player_hand = []
    dealer_hand = []
    dealer_hand_value = 0
    player_hand_value = 0
    
    while chips < 0:
        cardAdd(values, values_list, suit, suits_list)
        player_decision = input(f"Your card is {gen_card}, would you like to hit or stay?")
        
        if player_decision.lower() == "hit":
            player_hand.append(gen_card)
            player_hand_value = player_hand_value + values_list[gen_card]
            print(f"Here is your hand: {player_hand}. \n Here is the value of your hand in numbers: {player_hand_value}")
        
        elif player_decision.lower() == "stand":
            print(f"Here is your hand: {player_hand}. \n Here is the value of your hand in numbers: {player_hand_value}")


main()