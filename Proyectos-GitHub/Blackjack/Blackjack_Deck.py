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
        bet = int(input("Enter your bet: "))
        credits -= bet
        hand = 0
        dealer = 0
        win = False
        lose = False
        print(play_deck.length_of_deck())
        take = play_deck.take_card()
        take1 = its_a_number(take.number)
        hand += take1
        print("Your first card is a", take)
        first_ace = False
        if hand == 11:
            first_ace = True
        take = play_deck.take_card()
        take1 = its_a_number(take.number)
        dealer += take1
        print("Dealers first card is", take)
        dealer_ace = False
        if dealer == 11:
            dealer_ace = True
        dealer_first_play = True
        take = play_deck.take_card()
        take1 = its_a_number(take.number)
        print("Your second card is a", take)
        ace = False
        if take1 == 11:
            ace = True
        hand += take1
        if hand == 21:
            print("Blackjack!!!")
            win = True
        if hand > 21:
            lose = True
            if ace and first_ace:
                hand -= 10
                lose = False
                first_ace = False
        answer = ""
        while not win and not lose and answer != "stay" and answer != "double":
            print("You have a hand of", hand)
            answer = input("What do you want to do? (you can hit, stay or double) ")
            answer = answer.lower()
            if answer == "hit":
                take = play_deck.take_card()
                take1 = its_a_number(take.number)
                print("You draw a", take)    
                hand += take1
                if hand > 21 and ace:
                    ace = False
                    hand -= 10
                if take1 == 11:
                    ace = True
                if hand > 21 and ace:
                    ace = False
                    hand -= 10
            elif answer == "double":
                credits -= bet
                bet = bet*2
                take = play_deck.take_card()
                take1 = its_a_number(take.number)
                print("You draw a", take)
                hand += take1
                if hand > 21 and ace or hand > 21 and first_ace:
                    ace = False
                    hand -= 10
                if take1 == 11:
                    ace = True
                if hand > 21 and ace:
                    ace = False
                    hand -= 10
        while dealer < 17:
            take = play_deck.take_card()
            take1 = its_a_number(take.number)
            print("The dealer draw a", take)
            dealer += take1
            if dealer == 21 and dealer_first_play:
                print("Dealers Blackjack!")
                lose = True
            if dealer_ace > 21 and dealer_ace:
                dealer -= 10
            if take1 == 11:
                dealer_ace = True
            if dealer_ace > 21 and dealer_ace:
                dealer -= 10
            print("The dealer has a hand of", dealer)
        if hand > 21:
            lose = True
        if win and lose:
            print("It's a deuce")
            credits += bet
        elif win and not lose:
            print("You win!!")
            credits += bet*2
        elif not win and lose:
            print("You lose")
        else:
            if hand > dealer:
                print("You win!!")
                credits += bet*2
            elif hand == dealer:
                print("It's a deuce")
                credits += bet
            elif hand < dealer:
                print("You lose")
        answer2 = input("Do you want to keep playing? (only yes/no answer) ")
        if answer2 == "no":
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
        a = bj_deck.create_deck()
        bj_deck.shuffle()
        print(bj_deck.length_of_deck())
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