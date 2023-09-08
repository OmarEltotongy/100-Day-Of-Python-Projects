## Lists of Dictionaries
#Project idea: Travel Tracker
## For illustration:

# my_list = [
#     {"name": "Alice", "age": 30},
#     {"name": "Bob", "age": 25},
#     {"name": "Charlie", "age": 35}
# ]

# You can use a for loop to iterate over each dictionary in the list and access its key-value pairs like this:

# for person in my_list:
#     print("Name:", person["name"])
#     print("Age:", person["age"])
#     print()  # Just for adding an empty line between each person

#################################################
import os #For clearing the screen
import art

def clear_screen():
    os.system('cls')

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country,visits,cities ):
#     travel_log.append({"country": country , "visits": visits , "cities": cities})


# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

############################################################################################
print(art.logo)

print("Welcome to the secret auction program.\n")

def add_new_bidders(name,bid_amount ):
    bidders.append({"Name": name ,"Amount": bid_amount})

bidders= []
continue_state = True
Name_of_winner =""
Max_bid_amount=0

while(continue_state):
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $")) #Must be converted
    add_new_bidders(name,bid)



    for bidder in bidders:
        if(bidder["Amount"]) > Max_bid_amount:
            Max_bid_amount = bidder["Amount"]
            Name_of_winner = bidder["Name"]



#Wrong one
    # for key in bidders:
    #     if(bidders[key]) > Max_bid_amount:
    #         Max_bid_amount = bidders[key]
    #         Name_of_winner = bidders[key]

    decision = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if (decision == "no"):
        print(f"The winner is {Name_of_winner} with a bid of ${Max_bid_amount}")
        continue_state = False
    elif(decision == "yes"):
        clear_screen()


