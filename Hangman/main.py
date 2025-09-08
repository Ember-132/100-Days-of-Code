import random
from word_list import word_list
import hangman_drawings as hd

#----------------------------------------------------------------------------------- FUNCTIONS

def game_complete():
    '''Check if all letters have been guessed correctly, and if so, return True'''
    incorrect_char = 0
    correct_char = 0
    letter_match2 = 0
    for letter in list_word:
            if letter != "_":
                correct_char += 1
                letter_match2 +=1
                if letter_match2 == len(random_word):
                    if incorrect_char >= 1:
                        return False
                    else:
                        print("WINNER! You completed the game!")
                        print(f"\nThe word was: {random_word}")
                        return True
            elif letter == "_":
                letter_match2 += 1
                incorrect_char += 1
                if letter_match2 == len(random_word):
                    if incorrect_char >= 1:
                        return False
                    else:
                        print("WINNER! You completed the game!")
                        return True
        

def show_hangman():
    '''Show the hangman dependant on how many lives the user has left'''
    if lives == 8:
        print(hd.hangman_8)
    elif lives == 7:
        print(hd.hangman_7)
    elif lives == 6:
        print(hd.hangman_6)
    elif lives == 5:
        print(hd.hangman_5)
    elif lives == 4:
        print(hd.hangman_4)
    elif lives == 3:
        print(hd.hangman_3)
    elif lives == 2:
        print(hd.hangman_2)
    elif lives == 1:
        print(hd.hangman_1)

#----------------------------------------------------------------------------------- MAIN CODE

#PRINT WELCOME SCREEN
print(hd.hangman_logo)
print(hd.hangman_0)


#CHOOSE A RANDOM WORD FROM THE WORD LIST
random_word = random.choice(word_list)
random_word_length = len(random_word)

#SEPERATE RANDOM WORD INTO [A, B, C] FORMAT
list_word = [random_word[0]]
index_number1 =0
for char in range(0, random_word_length-1):
    index_number1 += 1
    list_word.append(random_word[index_number1])
#PRINT THE WORD WITH '_''S TO SHOW HOW MANY LETTERS ARE NEEDED. ALSO PRINT THE NUMBER OF LETTERS NEEDED
index_number2 = 0
for char in range(0, random_word_length):
    list_word[index_number2] = "_"
    index_number2 += 1
print(f"Your word to guess has {random_word_length} characters:")
print(list_word)

#MAIN BODY OF CODE. WHILE GAME ISN'T YET WON, REPEAT UNTIL 15 TURNS HAVE BEEN TAKEN.
lives = 8
turns = 0
guessed_letters=[]

#WHILE GAME HAS NOT YET BEEN WON
while game_complete() == False:
    
    if lives > 0:
        
        if turns >= 1:
            print(f"Number of lives left = {lives}")
            print(f"Guessed letters = {guessed_letters}")
            print(f"\n{list_word}")

        guess = input("\nTry and guess the word by typing a letter! : ")
        #CHECK GUESS IS A LETTER. IF IT ISN'T, PROMPT USER TO RE-ENTER
        while not guess.isalpha():
            guess = input(f"\n'{guess}' is not a letter, please choose a letter : ")  
        #CHECK GUESS IS A LETTER THAT HASN'T BEEN GUESSED YET. IF IT HAS, PROMPT USER TO RE-ENTER
        while guess in guessed_letters:
            guess = input(f"\nYou already guessed '{guess}', choose a different letter : ")     
                        
        guessed_letters.append(guess)
        turns += 1
        

        letter_match = 0
        incorrect_char = 0
        correct_char = 0
        
        #CHECK IF LETTER IS CORRECT, THEN DISPLAY THE APPROPRIATE MESSAGE AND HANGMAN SYMBOL
        for letter in random_word:
            if letter == guess:
                list_word[letter_match] = guess
                letter_match += 1
                correct_char += 1
                if letter_match == random_word_length and correct_char >= 1:
                    show_hangman()
                    print("\nWell done! You got a letter right!")
            elif letter != guess:
                letter_match += 1
                incorrect_char += 1
                if incorrect_char == random_word_length:
                    lives -= 1
                    if lives > 0:
                        show_hangman()
                        print("\nBad guess. Try Again..")
                elif letter_match == random_word_length and correct_char >= 1:
                    show_hangman()
                    print("\nWell done! You got a letter right!")
        
    #IF GAME OVER
    else:
        print(hd.game_over_logo)
        print("\nYou ran out of lives.")
        print(f"\nThe word was: {random_word}")
        print(hd.hangman_0)
        break
    