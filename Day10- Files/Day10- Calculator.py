import art
import os

def clear_screen():
    os.system('cls')

def add(n1,n2):
    return n1+n2

def multiply(n1,n2):
    return n1*n2

def subtract(n1,n2):
    return n1-n2

def divide(n1,n2):
    return n1/n2

continue_number = 1
result = 0
print (art.logo)
n1 = float(input("Enter ur first Number: "))

while(continue_number):
    sign = input("Enter the sign of operation: + , - , * , / : ")

    n2= float(input ("Enter ur second number: "))


    if(sign == '+'):
        result = add(n1,n2)
        print(f"The calculated number is: {result}\n")

    elif (sign == '-'):
        result = subtract(n1,n2)
        print(f"The calculated number is: {result}\n")

    elif (sign == '/'):
        result = divide(n1,n2)
        print(f"The calculated number is: {result}\n")

    elif (sign == '*'):
        result = multiply(n1,n2)
        print(f"The calculated number is: {result}\n")

    else: 
        print("Enter a valid sign \n")

    continue_number= int(input(f"Type '1' if u want to continue with {result} for more calculation and '0' for terminating \n"))
    if continue_number == 1:
        n1 = result
        clear_screen()
        print (art.logo)

