import random

#define ranks and suits
# indeces 0     1   2    3   4     5    6    7     8    9    10   11  12
ranks: tuple[str] = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K","A")
suits: tuple[str] = ("hearts", "diamonds", "clubs", "spades")

#make deck and shuffle
deck: list[tuple[str,str]] = [(rank, suit)for rank in ranks for suit in suits]

random.shuffle(deck)
p2_hand = deck[26:]
p1_hand = deck[:26]

#p1_card = p1_hand[0]
#p2_card = p2_hand[0] (maybes)
p1_card = [p1_hand.pop(0) for _ in range(26)]
p2_card = [p2_hand.pop(0) for _ in range(26)]

#deal deck (2 players)
#each player plays a card
def card_comparison(p1_card, p2_card):
    while (len(p1_hand) > 0) and (len(p2_hand) > 0):
        
        # we want to convert "5" to its index in ranks
        # ranks.index("5") => 3
        print(f"You have {len(p1_hand)} cards in your current deck")
        print(f"You played {p1_hand[0]}")
        print(f"Your opponent played {p2_hand[0]}")

        card_comparison(p1_card[0], p2_card[0])
        if ranks.index(p1_card[0]) > ranks.index(p2_card[0]):
            return 1 and print("You won this round!")
            
        #p2_hand.pop(0) = p1_hand

        elif ranks.index(p2_card[0]) > ranks.index(p1_card[0]):
            return 2 and print(f"You lost this round :(")
        #    p1_hand.pop(0) = p2_hand

        else:
            return 0 and print("PEACE!!")
        print("_______________________________________________________")


# while _________:
# in the underscore, we put a condition that is true or false
# run so long as both players have cards
#   this indented, and will run as long as loop is True

#whichever person has the higher rank recieves both cards
#if it's a tie, it goes to war!
#if war: each person plays three cards and then the fourth is compared. when someone wins, they get all the cards
#repeat until someone wins all the cards

card_comparison(p1_card, p2_card)


