# to randomly choose between a dict, u should use it like it: person= random.choice(data)
# In Python, the underscore character (_) is often used as a variable name when you want to indicate that you are not going to use the value of that variable.
# It's a convention to signal to other programmers (and to yourself) that the value of this variable is not important in the current context.

import art
import random
import os

def clear_screen():
    os.system('cls')

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'a Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'a Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'a Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Elon Musk',
        'follower_count': 100,
        'description': 'an Entrepreneur and CEO of SpaceX and Tesla',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 226,
        'description': 'a Reality TV star and entrepreneur',
        'country': 'United States'
    },
    {
        'name': 'Bill Gates',
        'follower_count': 54,
        'description': 'a Co-founder of Microsoft and philanthropist',
        'country': 'United States'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 144,
        'description': 'a Singer-songwriter',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 250,
        'description': 'an Actor and former professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 238,
        'description': 'a Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 219,
        'description': 'a Singer and actress',
        'country': 'United States'
    }
]

print(art.logo)
print("Welcome to Higher Lower Game.\n")
A = 0
B = 0
more_followers=0
points_counter = 0

counter_for_loop =0

while(True):
    if(points_counter == 9):
        print("Nice Work. u Completed the game, wait for more challenges.\n")
        break
    while(counter_for_loop <2):

        person_a= random.choice(data)
        person_b= random.choice(data)

        while person_a == person_b:  # Ensure person_a and person_b are distinct
            person_b = random.choice(data)

        if counter_for_loop == 0:
            print(f"Compare between A: {person_a['name']}, {person_a['description']}, {person_a['country']} \n")
            A = person_a['follower_count']
            print(art.vs)
            counter_for_loop+= 1
        elif counter_for_loop == 1:
            print(f"Against B: {person_b['name']}, {person_b['description']}, {person_b['country']} \n")
            B = person_b['follower_count']
            counter_for_loop+=1
    
    counter_for_loop = 0
    #Marking who has more follower count:
    if (A > B):
        more_followers = A
    else:
        more_followers = B

    user_guess = input("Who has  more followers? Type 'A' or 'B': " ).upper()
    if(user_guess == 'A' and more_followers == A):
        points_counter +=1
        clear_screen()
        print(art.logo)
        print(f"You're right! Current score: {points_counter}.\n")
    elif(user_guess == 'B' and more_followers == B):
        points_counter +=1
        clear_screen()
        print(art.logo)
        print(f"You're right! Current score: {points_counter}.\n")
    elif(user_guess == 'A' and more_followers == B):
        print(f"Sorry, that's wrong. Final score: {points_counter}\n")
        break
    elif(user_guess == 'B' and more_followers == A):
        print(f"Sorry, that's wrong. Final score: {points_counter}\n")
        break
    else:
        clear_screen()
        print(art.logo)
        print(f"It's not counted, Current score: {points_counter}.\n")
        print("Please enter a valid input.")
        
