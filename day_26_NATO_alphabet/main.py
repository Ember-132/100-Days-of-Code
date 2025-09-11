# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

##Looping through dictionaries:
# for (key, value) in student_dict.items():
    ##Access key and value
    # pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

##Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    ##Access index and row
    ##Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

# read the csv 
code_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# create a dictionary from the read data
dictionary = {row.letter:row.code for (index, row) in code_df.iterrows()}

on = True
while on:

    # prompt user for a work and convert it to upper case
    word = input("Please write a word: ").upper()

    # print NATO word for each letter in the word entered. Produce an error if user enters a non-letter
    try:
        output = [dictionary[letter] for letter in word]
    except KeyError:
        print("Please only type letters")
    else:
        print(output)