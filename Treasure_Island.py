print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`.",` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
turn = input("You're at the cross road. Where do you want to go? Type 'left' or 'right' ").lower()
#  input('You\'re at the cross road. Where do you want to go? Type "left" or "right".')
if turn == "left":
  lake = input("You have come to a lake. There is an island at the middle of a lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
  if lake == "wait":
    door = input("You have arrived at the island unharmed.There is a house with 3 doors. One red, one blue, one yellow. Which colour do you choose? ").lower()
    if door == "yellow":
      print("You found the treasure. You Win!")
    elif door == "blue":
      print("Eaten by beasts.\nGame Over!")
    elif door == "red":
      print("Burned by fire.\nGame Over!")
    else:
      print("Game Over!")
  else:
    print("Attacked by trout.\nGame Over!")
else:
  print("Fallen into a hole.\nGame over!")
