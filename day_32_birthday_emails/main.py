import datetime as dt
import smtplib
import pandas
import random

# your email and password
my_email = "xxxxxxx"
password = "xxxxxxx"

# get todays date in (month, day) format
now = dt.datetime.today()
today = (now.month,now.day)

# read the csv and save data as a dictionary
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]): data_row for (index,data_row) in data.iterrows()}

# if it's someone in the file's birthday today
if today in birthday_dict:
    person_data = birthday_dict[today]
    # choose a random letter from the letter templates folder and replace [NAME] with their name
    iteration = random.randint(1,3)
    file_path= f"letter_templates/letter_{iteration}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]",person_data["name"])
    # create/overwrite 'new_letter' with the birthday letter
    with open("new_letter.txt","w") as new_letter:
        new_contents = new_letter.write(contents)
    
    # EXTRA: Send an email and a quote to the birthday person containing the message
    person_email = person_data["email"]
    # choose a random quote
    with open("quotes.txt","r") as quotes:
        quotes = quotes.readlines()
    random_quote = random.choice(quotes)
    # send email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=person_email, # this should be birthday persons email from the file
            msg=f"Subject:Happy Birthday!\n\n{contents}\n\n{random_quote}"
        )
    





