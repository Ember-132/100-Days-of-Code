logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random


# MY FUNCTIONS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def get_user_card():
    user_random_card = random.choice(cards)
    user_cards.append(user_random_card)
    cards.remove(user_random_card)

def get_computer_card():
    computer_random_card = random.choice(cards)
    computer_cards.append(computer_random_card)
    cards.remove(computer_random_card)

def show_computers_cards():
    print("The computers cards are:")
    print(computer_cards)

def show_users_cards():
    print("Your cards are:")
    print(user_cards)

def who_wins():
    if sum(user_cards) > 21:
        if sum(computer_cards) > 21:
            print("YOU BOTH LOSE")
            show_users_cards()
            show_computers_cards()
        else:
            print("YOU LOSE")
            show_users_cards()
            show_computers_cards()
    elif sum(computer_cards) > 21:
        if sum(user_cards) > 21:
            print("YOU BOTH LOSE")
            show_users_cards()
            show_computers_cards()
        else:
            print("YOU WIN")
            show_users_cards()
            show_computers_cards()
    elif sum(user_cards) == sum(computer_cards):
        print("YOU DRAW")
        show_users_cards()
        show_computers_cards()
    elif sum(user_cards) > sum(computer_cards):
        print("YOU WIN")
        show_users_cards()
        show_computers_cards()
    elif sum(user_cards) < sum(computer_cards):
        print("YOU LOSE")
        show_users_cards()
        show_computers_cards()
    else:
        print("Error")


# MAIN CODE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print(logo)

replay = True
while replay:

    # CARD LIST >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user_cards = []
    computer_cards = []
    get_user_card()
    get_computer_card()
    get_user_card()
    print("\nYour cards are: ")
    print(user_cards)
    print("The computers first card is:")
    print(computer_cards)


    def check_ace():
        ace_card = user_cards.index(11)
        user_cards[ace_card] = 1
        print("Your blackjack has been changed from 11 to a 1")
        show_users_cards()


    end_of_game = False

    while not end_of_game:
        if sum(user_cards) < 21:
            choice = input('Type "hit" or "stand": ')
            if choice == "hit":
                get_user_card()
                if sum(computer_cards) < 21:
                    get_computer_card()
                if sum(user_cards) == 21:
                    end_of_game = True
                elif sum(user_cards) > 21:
                    if 11 in user_cards:
                        check_ace()
                    else:
                        end_of_game = True
                else:
                    show_users_cards()
            elif choice == "stand":
                while sum(computer_cards) < 17:
                    get_computer_card()
                end_of_game = True
    who_wins()
    play_again = input('Would you like to play again? Type "y" for yes and "n" for no: ')
    if play_again == "n":
        replay = False
        print("GAME ENDED")
