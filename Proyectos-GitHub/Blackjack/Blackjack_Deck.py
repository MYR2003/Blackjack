from Class_card_and_deck import card
from Class_card_and_deck import deck
from random import randrange as rand

def its_a_number(numb):
    if not numb.isdigit():
        if numb != "Ace":
            return 10
        else:
            return 11
    else:
        return int(numb)

def blackjack(credits, play_deck):
    print("Welcome to Blackjack!")
    while 0 < credits:
        bet = input("Enter your bet: ")
        credits -= bet
        hand = 0
        dealer = 0
        take = play_deck.take_card()
        take = its_a_number(take.number)
        hand += take
        print("Your first card is a", take)
        first_ace = False
        if hand == 11:
            first_ace = True
        take = play_deck.take_card()
        take = its_a_number(take.number)
        dealer += take
        print("Dealers first card is", take)
        dealer_ace = False
        if dealer == 11:
            dealer_ace = True
        

        win = False
        lose = False
        while not win and not lose:
            break
        
    return credits


credits = 1000
while credits > 0:
    print("What do you want to do, here are your options:")
    print("To play blackjack enter 1")
    print("To quit playing enter 0")
    answer = input("Enter your answer here: ")
    if answer == "1":
        bj_deck = deck(6)
        credits = blackjack(credits, bj_deck)
    elif answer == "0":
        print("Thank you for playing :)")
        break

if credits < 0:
    print("Bankruptcy")
elif credits == 0:
    print("You have no more credits to play")
else:
    print("You left with", credits, "credits")