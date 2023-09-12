############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

import random
import art

def Print_Cards():
    print(f"Ur cards are {user_cards}\n")
    print(f"Computer cards are {computer_cards}\n")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = [random.choice(cards), random.choice(cards)]
computer_cards= [random.choice(cards), random.choice(cards)]

print(art.logo)
print("Welcome to Blackjack Game\n\n")
print(f"Ur cards are[{user_cards[0]},{user_cards[1]}]\n")
print(f"Computer first card is: {computer_cards[0]}\n")

total_cards_for_computer = sum(computer_cards)  
total_cards_for_user = sum(user_cards)


while(True):

    if (total_cards_for_computer == 21):
        Print_Cards()
        print("Computer has an ace, good luck next time\n")
        break
    elif (total_cards_for_computer == 21 and total_cards_for_user == 21):
        Print_Cards()
        print("Computer has an ace, good luck next time\n")
        break
    elif (total_cards_for_user == 21 ):
        Print_Cards()
        print("U won,U have an ace, Congrats\n")
        break
    elif (total_cards_for_user > 21):
        if (user_cards[0] == 11):
            user_cards[0] = 1
            total_cards_for_user = sum(user_cards)
            if(total_cards_for_user > 21):
                Print_Cards()
                print("U are still over 21 , good luck next time\n")
                break

        elif (user_cards[1]== 11):
            user_cards[1] = 1
            total_cards_for_user = sum(user_cards)

            if(total_cards_for_user > 21):
                Print_Cards()
                print("U are still over 21 , good luck next time\n")
                break

        else:
            Print_Cards()
            print("U are over 21 , good luck next time\n")
            break
    
    option = input("Do u want to get another cards type 'y' for yes and 'n' for no: ")
    if (option == 'y'):
        user_cards.append(random.choice(cards))
        total_cards_for_user = sum(user_cards)
        continue
    elif(option == 'n'):
        while(total_cards_for_computer < 17):
            computer_cards.append(random.choice(cards))
        if(total_cards_for_computer > 21):
            Print_Cards()
            print("U won, computer has over 21\n")
            break
        elif(total_cards_for_computer > total_cards_for_user):
            Print_Cards()
            print("Computer has more points than u,U lost \n")
            break
        elif(total_cards_for_computer < total_cards_for_user):
            Print_Cards()
            print("U have more points than computer,U won\n ")
            break
        elif(total_cards_for_computer == total_cards_for_user):
            Print_Cards()
            print("That's a draw, No one won\n")
            break


