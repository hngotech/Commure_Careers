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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
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
print("Your mission is to find the treasure.\n") 
choice1 = input("You\'re at a crossroad. Choose your destiny. Type 'Left' or 'Right'\n").lower()
if choice1 == "left":
    choice2 = input("You\'ve reached a body of water. Shall we swim or wait? Type 'Swim' or 'Wait'\n").lower()
    if choice2 == "wait":
      choice3 = input("Good job waiting. You were picked up by a flock of seagulls and arrive at the island unharmed and full of confidence. There is a gingerbread house with 3 doors. One red, one yellow, and one blue. Which color do you choose? Choose wisely.\n").lower()
      if choice3 == "red":
        print("You enter a room full of 100 unsolved rubiks cubes. You must complete them all before moving on. In other words, game over.")
      elif choice3 == "yellow":
        print("Well look what we have here! Could it be? Have you found the treasure? Yes, yes you have! Winner winner chicken dinner!")
      elif choice3 == "blue":
        print("You enter a room full of Wizzrobes and have lost your Master Sword! You also have zero weapons and zero armor. In other words, game over.")
    else:      
      print("Whoa whoa whoa whoa WHOA! Did you not see the crushing current and crocodile heads floating on the surface staring right at you? You. Are. Dead. Done. Game Over.")
else:
  print("dunh, dunh, duuuunh, you have fallen into a pit of vipers! Game. Over.")
