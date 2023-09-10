import Art
import random


def Guessing_function(mode):
    if(mode == 'easy'):
        print(f"You have {easy_mode} attempts remaining to guess the number.\n")
        guess = int(input("make a guess: "))
        if (guess > my_number):
            while(easy_mode>0):
                print("Too high.\nGuess again.")
                break
        elif(guess < my_number):
            while(easy_mode>0):
                print("Too low.\nGuess again.")
                break
        elif (guess == my_number):
            return True
    elif(mode == 'hard'):
        print(f"You have {hard_mode} attempts remaining to guess the number.\n")
        guess = int(input("make a guess: "))
        if (guess > my_number):
            while(hard_mode>0):
                print("Too high.\nGuess again.")
                break
        elif(guess < my_number):
            while(hard_mode>0):
                print("Too low.\nGuess again.")
                break
        elif (guess == my_number):
            return True

print(Art.Logo)
print("Welcome to the  Number Guessing Game\n")

my_number = random.randint(0,101)
print(f"For debugging, My number is {my_number}")

print("I'm Thinking of a number between 0 and 100.  \n")
mode = input("Choose a difficulty. Type 'easy' or ' hard: ").lower()
easy_mode = 10
hard_mode = 5


if (mode == 'easy'):
    while(easy_mode != 0):
        state = Guessing_function(mode)
        easy_mode = easy_mode - 1
        if(state == True):
            print(f"U got it the answer was {my_number}")
            break
elif (mode == 'hard'):
    while(hard_mode != 0):
        state =Guessing_function(mode)
        hard_mode = hard_mode - 1
        if(state == True):
            print(f"U got it the answer was {my_number}")
            break
elif(mode != 'easy' and mode != 'hard'):
    print("Please Enter a valid mode\n")

if(easy_mode == 0 or hard_mode ==0):
    print(f"You have {easy_mode} attempts remaining to guess the number.\n")
    print("U 've run out of guesses, u lost\n")
