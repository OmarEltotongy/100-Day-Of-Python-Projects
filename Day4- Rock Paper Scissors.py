# # input.split(', ') to remove something and put them to a list instead.
#output = random.randint(0,len(options)-1)


# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# horizontal = int(position[0])    
# vertical = int(position[1])
# map[vertical-1][horizontal-1] = "💎"

# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

################################################################
#Project Day 4
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

true_length = len(options) - 1

output = random.randint(0, true_length)

chose = int(input('What do you want to choose? 0 For Rock, 1 For Paper, or 2 For Scissors\n'))

# Rock was chosen
if chose == 0:
    if output == 0:  # Rock
        print(options[output])
        print(options[chose])
        print('Draw')
    elif output == 1:  # Paper
        print(options[output])
        print(options[chose])
        print('Lost')
    elif output == 2:  # Scissors
        print(options[output])
        print(options[chose])
        print('Won')

# Paper was chosen
elif chose == 1:
    if output == 0:  # Rock
        print(options[output])
        print(options[chose])
        print('Won')
    elif output == 1:  # Paper
        print(options[output])
        print(options[chose])
        print('Draw')
    elif output == 2:  # Scissors
        print(options[output])
        print(options[chose])
        print('Lost')

# Scissors was chosen
elif chose == 2:
    if output == 0:  # Rock
        print(options[output])
        print(options[chose])
        print('Lost')
    elif output == 1:  # Paper
        print(options[output])
        print(options[chose])
        print('Won')
    elif output == 2:  # Scissors
        print(options[output])
        print(options[chose])
        print('Draw')