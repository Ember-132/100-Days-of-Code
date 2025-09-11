import art
from game_data import data
import random

def choose_random_list_item():
    """chooses a random number in the number of entries in the list data"""
    random_index = random.randint(0,len(data)-1)
    return random_index

def print_intel(index_list):
    """prints the celeb information in a specified format"""
    print(f"{data[index_list]['name']}, a {data[index_list]['description']}, from {data[index_list]['country']}.")

def check_win(celeb_1_followers, celeb_2_followers, user_guess):
    """compare the follower count between celebs to check if guess is correct. Return correct or not"""
    if celeb_1_followers > celeb_2_followers:
        return guess == "A"
    else:
        return guess == "B"


print(art.logo)
# assigns a random index to represent someone in the list
celeb_a_index = choose_random_list_item()
end_game = False
score = 0
while not end_game:
    print("Compare A:")
    print_intel(celeb_a_index)
    print(art.vs)
    print("Against B:")
    celeb_b_index = choose_random_list_item()
    # make sure the celeb doesn't end up comparing to itself
    while celeb_b_index == celeb_a_index:
        celeb_b_index = choose_random_list_item()
    print_intel(celeb_b_index)

    guess = input("Who has more followers? 'A' or 'B'?: ").upper()

    celeb_a_followers = data[celeb_a_index]['follower_count']
    celeb_a_followers_readable = data[celeb_a_index]['follower_count_readable']
    celeb_a_name = data[celeb_a_index]['name']
    celeb_b_followers = data[celeb_b_index]['follower_count']
    celeb_b_followers_readable = data[celeb_b_index]['follower_count_readable']
    celeb_b_name = data[celeb_b_index]['name']

    #runs the chosen celebs followers and the users guess though the check_win function to return if user was correct
    is_correct = check_win(celeb_1_followers=celeb_a_followers,celeb_2_followers=celeb_b_followers,user_guess=guess)

    # if statement for whether the user was correct
    if is_correct:
        score += 1
        print("\n" * 20)
        print(art.logo)
        print(f"\nYou got it right! {celeb_b_name} has {celeb_b_followers_readable} followers while {celeb_a_name} has {celeb_a_followers_readable}.")
        print(f"Your score is {score}")

    else:
        print(f"\nSorry, you were wrong. {celeb_b_name} has {celeb_b_followers_readable} followers while {celeb_a_name} has {celeb_a_followers_readable}")
        end_game = True
    # makes the previous B celebrity replace the celebrity in A
    celeb_a_index = celeb_b_index

print(f"You scored a total of {score}")

