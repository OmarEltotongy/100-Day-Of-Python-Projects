import random
import hangman_art as hangman_art
import hangman_words as hangman_words

# #Step 1 

# word_list = ["aardvark", "baboon", "camel"]

# #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# chosen_word = random.choice(word_list)

# #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("Please choose a letter: ").lower() #for safety reasons.

# print(chosen_word) #for debugging purposes

# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for  letter in range(len(chosen_word)): #Could be letter in chosen_word
#     if (guess == chosen_word[letter]):  #if (letter == guess)
#         print("Correct!")
#     else:
#         print("Wrong!")

#Step 2

# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #TODO-1: - Create an empty List called display.
# display = []

# for letter in range(len(chosen_word)):
#     display.append("_")

# guess = input("Guess a letter: ").lower()

# #TODO-2: - Loop through each position in the chosen_word;

# for letter in range(len(chosen_word)):
#     if guess == chosen_word[letter]:
#         display[letter] = guess

# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

# #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# print(display)

#Step 3

# #TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# display = []

# for letter in range(len(chosen_word)):
#     display.append("_")


# while "_" in display:
#     guess = input("Guess a letter: ").lower()
#     for letter in range(len(chosen_word)):
#         if guess == chosen_word[letter]:
#             display[letter] = guess
#     print(display)

# if "_" not in display:
#     print("U Won, Luckily :D")


#Step 4

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

    

# #TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
# #Set 'lives' to equal 6.

# lives = 6

# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# display = []

# for letter in range(len(chosen_word)):
#     display.append("_")

# #TODO-2: - If guess is not a letter in the chosen_word,
#     #Then reduce 'lives' by 1. 
#     #If lives goes down to 0 then the game should stop and it should print "You lose."

# #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
# while "_" in display:
#     guess = input("Guess a letter: ").lower()
#     if guess not in chosen_word:
#         print ("Wrong guess")
#         print(stages[lives])
#         lives -= 1
    
#     if lives == 0:
#         print(stages[lives])
#         print("You lose.")
#         print ("Wrong guess")
#         break

#     for letter in range(len(chosen_word)):
#         if guess == chosen_word[letter]:
#             display[letter] = guess
#     print(display)

# if "_" not in display:
#     print("U Won, Luckily :D")

#Step 5



#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#TODO-2: - Import the stages from hangman_art.py and make this error go away.
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
#TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

lives = 6

chosen_word = random.choice(hangman_words.word_list)

print("Welcome To Our Game:\n" + hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for letter in range(len(chosen_word)):
    display.append("_")

    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

while "_" in display:
    guess = input("Guess a letter: ").lower()

    
    if guess in display:
        print("U have already guessed this letter before. I will not charge u a life for that.")
    
    elif guess not in chosen_word:
        print (f"Wrong guess, The letter {guess} is not in the word, that cost a life.")
        print(hangman_art.stages[lives])
        lives -= 1

    if lives == 0:
        print (f"Wrong guess, The letter {guess} is not in the word, that cost a life.")
        print(hangman_art.stages[lives])
        print(f"You lose, The correct guess was {chosen_word}")

        break

    for letter in range(len(chosen_word)):
        if guess == chosen_word[letter]:
            display[letter] = guess
    print(display)

if "_" not in display:
    print("U Won, Luckily :D")

