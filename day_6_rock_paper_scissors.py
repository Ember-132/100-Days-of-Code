import random

options = ["ROCK", "PAPER", "SCISSORS"]

user_choice = int(input('What do you choose? Type "0" for Rock, "1" for Paper or "2" for Scissors: '))

computer_choice = random.randint(0,2)

if user_choice >= 3 or user_choice < 0:
    print("Invalid number")
else:
    print(f"You chose "+options[user_choice])
    print(f"The computer chose "+options[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose!")
    elif computer_choice > user_choice:
        print("You Lose!")
    elif user_choice > computer_choice:
        print("You Win!")
    elif computer_choice == user_choice:
        print("It's a Draw")
