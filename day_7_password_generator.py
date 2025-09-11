import random

print("Welcome to the PyPassword Generator!")

# Stored number, symbol and number data
letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols_list = ["{", "}", "#", ",", "!", "_", "@", "/", "^", "?", "%", "&", "$", "(", ")", "£", "-"]
numbers_list = ["1", "2", "3", "4", "5", "6", "7", "8" , "9"]

# Ask the user how many letters, symbols and numbers they want in their password
number_of_letters = int(input("How many letters would you like in your password? "))
number_of_symbols = int(input("How many symbols would you like? "))
number_of_numbers = int(input("How many numbers would you like? "))

# Choose random chars from each list, the number of chars is dependent on previous user entry
password_list = []
for char in range(0, number_of_letters):
    random_letter = random.choice(letters_list)
    password_list += random_letter

for char in range(0, number_of_symbols):
    random_symbol = random.choice(symbols_list)
    password_list += random_symbol

for char in range(0, number_of_numbers):
    random_number = random.choice(numbers_list)
    password_list += random_number

# Randomise the characters in the first iteration above
random.shuffle(password_list)

# Print the new password as a string
print(f"Your new password is: {''.join(password_list)}")

