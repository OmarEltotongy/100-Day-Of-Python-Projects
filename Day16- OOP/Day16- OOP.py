# from turtle import  Turtle, Screen
# from prettytable import PrettyTable

# table = PrettyTable()

# #str , list

# table.add_column("Name",["Name1", "Name 2"])

# #table.align = "Type" of attribute

# print(table)
##############################################################
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)

#creating objects from classes
menu = Menu()
maker= CoffeeMaker()
money= MoneyMachine()
while(True):
    order = input("What would you like? ").lower()
    
    if(order =='report'):
        maker.report()
        money.report()
    elif(order == 'menu'):
        menu.get_items
    
    elif (order == 'espresso'):
        menu.find_drink('espresso')
        if maker.is_resource_sufficient(espresso) and money.make_payment(cost= money.money_received):
            maker.make_coffee(espresso)
    elif (order == 'latte'):
        menu.find_drink('latte')
        if maker.is_resource_sufficient(latte) and money.make_payment(cost= money.money_received):
            maker.make_coffee(latte)

    elif (order == 'cappuccino'):
        menu.find_drink('cappuccino')
        if maker.is_resource_sufficient(cappuccino) and money.make_payment(cost= money.money_received):
            maker.make_coffee(cappuccino)
        
    else:
        menu.find_drink(order_name= order)







