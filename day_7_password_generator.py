import random

print("Welcome to the PyPassword Generator!")

number_of_letters = int(input("How many letters would you like in your password? "))
number_of_symbols = int(input("How many symbols would you like? "))
number_of_numbers = int(input("How many numbers would you like? "))

letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols_list = ["{", "}", "#", ",", "!", "_", "@", "/", "^", "?", "%", "&", "$", "(", ")", "£", "-"]
numbers_list = ["1", "2", "3", "4", "5", "6", "7", "8" , "9"]


password_list = []
for char in range(0, number_of_letters):
    password_list += random.choice(letters_list)

for char in range(0, number_of_symbols):
    password_list += random.choice(symbols_list)

for char in range(0, number_of_numbers):
    password_list += random.choice(numbers_list)


#we then have to randomise the characters in the first iteration above

new_password = ""
for char in password_list:
    new_password += random.choice(password_list)

print(f"Your new password is: {new_password}")

