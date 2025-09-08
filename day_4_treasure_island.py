print('''Welcome to Treasure Island
Your mission is to find the treasure.
*****************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')


first_move = input("You're at a cross road. Where do you want to go? Please enter \"right\" or \"left\"").lower()

if first_move == "left":
    second_move = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim accross. ").lower()
    if second_move == "wait":
        third_move = input("You arrive at the island unharmed. There is a house with 3 doors - one red, one yellow and one blue. Which colour do you choose? ").lower()
        if third_move == "red":
            print("It's a room full of fire! GAME OVER")
        elif third_move == "yellow":
            print("The room sucks you into oblivion with forceful winds! GAME OVER")
        elif third_move == "blue":
            print("You open the door to find a room full of treasure! YOU WIN!")
        else:
            print("Please choose a valid option")
    elif second_move == "swim":
        print("You get eaten alive by sharks! GAME OVER")
    else:
        print("Please choose a valid option")
elif first_move == "right":
    print("You take the wrong turn and fall off a cliff. GAME OVER")
else:
    print("Please choose a valid option")
