import random

#define ranks and suits
# indices             0    1    2    3    4    5    6    7     8    9    10   11  12
ranks: tuple[str] = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K","A")
suits: tuple[str] = ("hearts", "diamonds", "clubs", "spades")

#make deck and shuffle
deck: list[tuple[str,str]] = [(rank, suit)for rank in ranks for suit in suits]

random.shuffle(deck)
p2_hand = deck[26:]
p1_hand = deck[:26]

def move_first_to_end(hand):
    hand.append(hand.pop(0))
 #after every round, the player that wins must take their card and also place it in the back of their hand

def if_peace(p1_hand, p2_hand, ranks): #PEACE!
    war_cards = [] #putting all the peace cards placed down into a list and giving it to the winner
    print("PEACE!!")
    print(f"Both players now must place down three cards and flip over the last")
    for _ in range(3): #creating loop that runs 3 times
        if len(p1_hand) > 1 and len(p2_hand) > 1: #making sure both players have at least 2 cards
            war_cards.extend([p1_hand.pop(0), p2_hand.pop(0)])
            #adds the cards to the list
        else:
            return #if one of the players doesnt have enough cards, it ends the loop and the other wins
    
    if len(p1_hand) > 0 and len(p2_hand) > 0: #as long as players have cards
        p1_card = p1_hand[0]
        p2_card = p2_hand[0]
        print(f"You played {p1_card} and your opponent played {p2_card}")

        if ranks.index(p1_card[0]) > ranks.index(p2_card[0]): #comparing the numbers of the fourth card played
            print("You won the peace!")
            p1_hand.extend(war_cards) #adds all of the cards in the War_cards list to p1's hand
            p1_hand.append(p2_hand.pop(0)) #taking card from p2 and putting it in p1's hand
            move_first_to_end(p1_hand)
            

        elif ranks.index(p2_card[0]) > ranks.index(p1_card[0]):
            print(f"You lost the peace!(haha)")
            p2_hand.extend(war_cards)
            p2_hand.append(p1_hand.pop(0))
            move_first_to_end(p2_hand)
            #basically the oppostie of the last one

        else: #If there's another tie
            war_cards.extend([p1_hand.pop(0), p2_hand.pop(0)]) #adds the tied cards to the list
            if_peace(p1_hand, p2_hand, ranks) #Calls the function to restart

def card_comparison( p1_hand, p2_hand, ranks):
    while (len(p1_hand) > 0) and (len(p2_hand) > 0): #While loop as long as both players have cards
        
        p1_card = p1_hand[0]
        p2_card = p2_hand[0]
        
        print(f"You have {len(p1_hand)} cards in your current deck")
        print(f"Your opponent has {len(p2_hand)} cards in their deck")
        input("Press enter to play next round")

       
        print(f"You played {p1_hand[0]} and your opponent played {p2_hand[0]}")

        if ranks.index(p1_card[0]) > ranks.index(p2_card[0]): #If p1 wins (comparing indices)
            print("You won this round!")
            p1_hand.append(p2_hand.pop(0)) #Takes card from p2, gives it to p1
            move_first_to_end(p1_hand)

        elif ranks.index(p2_card[0]) > ranks.index(p1_card[0]):
            print(f"You lost this round :(")
            p2_hand.append(p1_hand.pop(0))
            move_first_to_end(p2_hand)
            #opposite of last

        else: #if the indices are the same (PEACE)
            if_peace(p1_hand, p2_hand, ranks) #Calls function

    if p1_hand: #When player has all the cards
        print("You won the game!")
    else:
        print("You lost the game.")            

card_comparison(p1_hand, p2_hand, ranks) #Calling the main loop to start the game


