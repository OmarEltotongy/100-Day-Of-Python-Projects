# # Shuffle the password
# random.shuffle(password)

# # Convert the password list to a string
# password_str = ''.join(password)

import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Ensure the total length of the password does not exceed the sum of the requested characters
total_characters = nr_letters + nr_symbols + nr_numbers

# Check if the total_characters exceeds the available characters
if total_characters > len(letters) + len(symbols) + len(numbers):
    print("Error: The total number of characters requested exceeds the available characters.")


password = []
for L in range(nr_letters):
    password.append(random.choice(letters))

# for S in symbols:
    password.append(random.choice(symbols))

# for N in numbers:
    password.append(random.choice(numbers))

# Shuffle the password
random.shuffle(password)

# Convert the password list to a string
password_str = ''.join(password)

print(f"Password: {password_str}")
