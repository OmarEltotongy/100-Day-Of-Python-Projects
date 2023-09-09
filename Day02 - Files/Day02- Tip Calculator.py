#PEMDAS IS THE ORDER OF PROCESS () , ** , * , / , + , -
#Float division (//)
#Operations can be manipulated like that: int *= 2 , int /=2 
#f-string would be better if u want to print different data types , use {this curly braces} to put the variable 


#Project 2

print("Welcome to the Tip Calculator.\n")
bill= input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10 , 12, or 15? ")
people = input("How many people to split the bill? ")

tip = (float(bill) * (int(percentage)/100) + float(bill) ) / int(people)
rounded_tip = round(tip,2)

print(f"Each person should pay: $ {rounded_tip}")