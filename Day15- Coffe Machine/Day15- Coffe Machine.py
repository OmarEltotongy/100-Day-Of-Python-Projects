import Data

order = ""
my_money = 0

def check_resource(order):
    if (order  == 'espresso'):
        #Check for water
        if (Data.resources['water'] < Data.MENU['espresso']['ingredients']['water']):
            print("Run out of water, refill\n")
            return False
        if (Data.resources['water'] >= Data.MENU['espresso']['ingredients']['water']):
            Data.resources['water'] -=  Data.MENU['espresso']['ingredients']['water']
            print("Done water for espresso")
        #Check for coffee
        if (Data.resources['coffee'] < Data.MENU['espresso']['ingredients']['coffee']):
            print("Run out of coffee, refill\n")
            Data.resources['water'] +=  Data.MENU['espresso']['ingredients']['water']
            print("Returned consumed water")
            return False
        if (Data.resources['coffee'] >= Data.MENU['espresso']['ingredients']['coffee']):
            Data.resources['coffee'] -=  Data.MENU['espresso']['ingredients']['coffee']
            print("Done coffee for espresso")
            return True
        
    
    elif (order  == 'latte'):
        #Check for water
        if (Data.resources['water'] < Data.MENU['latte']['ingredients']['water']):
            print("Run out of water, refill\n")
            return False
        if (Data.resources['water'] >= Data.MENU['latte']['ingredients']['water']):
            Data.resources['water'] -=  Data.MENU['latte']['ingredients']['water']
            print("Done water for latte")

        #Check for coffee
        if (Data.resources['coffee'] < Data.MENU['latte']['ingredients']['coffee']):
            print("Run out of coffee, refill\n")
            Data.resources['water'] +=  Data.MENU['latte']['ingredients']['water']
            print("Returned consumed water")
            return False
        if (Data.resources['coffee'] >= Data.MENU['latte']['ingredients']['coffee']):
            Data.resources['coffee'] -=  Data.MENU['latte']['ingredients']['coffee']
            print("Done coffee for latte")
        
        #Check for milk
        if (Data.resources['milk'] < Data.MENU['latte']['ingredients']['milk']):
            print("Run out of milk, refill\n")
            Data.resources['coffee'] +=  Data.MENU['latte']['ingredients']['coffee']
            print("Returned consumed coffee")
            return False
        if (Data.resources['milk'] >= Data.MENU['latte']['ingredients']['milk']):
            Data.resources['milk'] -=  Data.MENU['latte']['ingredients']['milk']
            print("Done milk for latte")
            return True
    

    elif (order == 'cappuccino'):
        #Check for water
        if (Data.resources['water'] < Data.MENU['cappuccino']['ingredients']['water']):
            print("Run out of water, refill\n")
            return False
        if (Data.resources['water'] >= Data.MENU['cappuccino']['ingredients']['water']):
            Data.resources['water'] -=  Data.MENU['cappuccino']['ingredients']['water']
            print("Done water for cappuccino")

        #Check for coffee
        if (Data.resources['coffee'] < Data.MENU['cappuccino']['ingredients']['coffee']):
            print("Run out of coffee, refill\n")
            Data.resources['water'] +=  Data.MENU['cappuccino']['ingredients']['water']
            print("Returned consumed coffee")
            return False
        if (Data.resources['coffee'] >= Data.MENU['cappuccino']['ingredients']['coffee']):
            Data.resources['coffee'] -=  Data.MENU['cappuccino']['ingredients']['coffee']
            print("Done coffee for cappuccino")

        #Check for milk
        if (Data.resources['milk'] < Data.MENU['cappuccino']['ingredients']['milk']):
            print("Run out of milk, refill\n")
            Data.resources['coffee'] +=  Data.MENU['cappuccino']['ingredients']['coffee']
            print("Returned consumed coffee")
            return False
        if (Data.resources['milk'] >= Data.MENU['cappuccino']['ingredients']['milk']):
            Data.resources['milk'] -=  Data.MENU['cappuccino']['ingredients']['milk']
            print("Done milk for cappuccino")
            return True
        
def check_cost(order):
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_dollars = (quarters * 0.25) + (dimes * 0.1) + (pennies * 0.01) + (nickles * 0.05)
    
    if (order == 'espresso'):
        if(Data.MENU['espresso']['cost'] > total_dollars):
            print(f"Sorry, the cost for the espresso is {Data.MENU['espresso']['cost']} and u only payed {total_dollars}\nRefunded")
        elif(Data.MENU['espresso']['cost'] < total_dollars):
            print(f"Here is ${total_dollars - Data.MENU['espresso']['cost'] } in change")
            print("Here is your espresso ☕️. Enjoy!")

    elif(order == 'latte'):
        if(Data.MENU['latte']['cost'] > total_dollars):
            print(f"Sorry, the cost for the latte is {Data.MENU['latte']['cost']} and u only payed {total_dollars}\nRefunded")
        elif(Data.MENU['latte']['cost'] < total_dollars):
            print(f"Here is ${total_dollars - Data.MENU['latte']['cost'] } in change")
            print("Here is your latte ☕️. Enjoy!")

    elif(order == 'cappuccino'):
        if(Data.MENU['cappuccino']['cost'] > total_dollars):
            print(f"Sorry, the cost for the cappuccino is {Data.MENU['cappuccino']['cost']} and u only payed {total_dollars}\nRefunded")
        elif(Data.MENU['cappuccino']['cost'] < total_dollars):
            print(f"Here is ${total_dollars - Data.MENU['cappuccino']['cost'] } in change")
            print("Here is your cappuccino ☕️. Enjoy!")


while(True):
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if(order =='report'):
        for item in Data.resources:
            print(f"{item}: {Data.resources[item]}")
    elif (order == 'off'):
        break
    elif (order == 'espresso'):
        resources_state = check_resource('espresso')
        if(resources_state == True):    
            check_cost('espresso')
    elif (order == 'latte'):
        resources_state = check_resource('espresso')
        if(resources_state == True):    
            check_cost('latte')
    elif (order == 'cappuccino'):
        resources_state = check_resource('cappuccino')
        if(resources_state == True):    
            check_cost('cappuccino')

