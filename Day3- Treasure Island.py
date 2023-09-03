print(r'''                 ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')

print("Welcome to the Treasure Island\nUr mission is to find the treasure\n")

direction=input('u are at a cross road. Where do u want to go? Type "left" or "right"\n')
if direction.lower() == 'right':
  print("Game over")
else:
  decision=input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for the boat. type "swim" to swim across\n')
  if decision.lower() == 'swim':
    print("Game over")
  else:
    door=input('u arrived to the island unharmed. There is a house with 3 doors, One red, one yellow and one blue. Which color do u choose?\n')
    if door.lower() =='red' or door.lower() == 'green':
      print("Game over")
    else:
      print("WE HAVE A WINNER, CONGRATULATIONS")
