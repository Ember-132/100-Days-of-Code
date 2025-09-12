from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- VARIABLES ---------------------------- #
GREY = "#D8D2C2"
FONT_NAME = "Arial"
LETTERS = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
SP_CHAR = ["/","_","*",")","$","%","<","+","-","*","#"]

# ---------------------------- SEARCH ------------------------------- #
def search_info():
    '''Search for the user entry website and return an error if data not already stored'''
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            username_entry.insert(0,email)
            password_entry.insert(0, password)
        else:
            messagebox.showinfo(title="Error", message=f"There is no record saved for '{website}'")


# ---------------------------- 'ADD' TO FILE ------------------------------- #
def add_to_file():
    '''Adds an entry to the json file using a confirmation message box and shows errors if fields left empty'''
    
    # collect the data entered by the user and put it into dictionary format
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    # if fields left empty, produce error message
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error",message="Please don't leave fields empty")
    else:
        # if entered fields are valid, a message box is shown to the user for confirmation to add the new entry
        is_ok = messagebox.askyesno(title="Password Manager",
                                    message=f"Details entered: \n\nWebsite: {website}\nEmail/Username: "
                                            f"{email}\nPassword: {password}\n\nAre you sure you want"
                                            f" to add this to the log?")
        if is_ok:
            # try except clause to add the new data to the json and reset the entry fields
            try:
                with open("data.json","r") as data_file:
                    data = json.load(data_file)
            except:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                    website_entry.delete(0,END)
                    username_entry.delete(0, END)
                    password_entry.delete(0, END)
                    website_entry.focus()

# ---------------------------- 'GENERATE PASSWORD' FUNCTION ------------------------------- #
def generate_password():
    '''Generates a random password for the user'''
    new_pw = []
    for char in range(0,13):
        random_iteration = random.randint(1, 3)
        random_letter = random.choice(LETTERS)
        random_sp_char = random.choice(SP_CHAR)
        random_number = random.randint(1, 9)
        if random_iteration ==1:
            new_pw.append(random_letter)
        elif random_iteration == 2:
            new_pw.append(random_sp_char)
        else:
            new_pw.append(str(random_number))
    new_pw = ''.join(new_pw)
    password_entry.delete(0,END)
    password_entry.insert(0,new_pw)
    #copy password to clipboard
    pyperclip.copy(new_pw)

# ---------------------------- UI ------------------------------- #
# screen layout
screen = Tk()
screen.title("Password Manager")
screen.config(padx=50,pady=50,bg=GREY)

# logo
padlock = Canvas(width=200,height=200,bg=GREY, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
padlock.create_image(100,100,image = lock_image)
padlock.grid(column=1,row=0)

# labels
website_label = Label(text="Website:",bg=GREY,font=(FONT_NAME,10,"normal"))
website_label.grid(column=0,row=1, sticky="E")
username_label = Label(text="Email/Username:",bg=GREY,font=(FONT_NAME,10,"normal"))
username_label.grid(column=0,row=2, sticky="E")
password_label = Label(text="Password:",bg=GREY,font=(FONT_NAME,10,"normal"))
password_label.grid(column=0,row=3, sticky="E")

# text boxes for user entry
website_entry = Entry(width=30)
website_entry.grid(column=1,row=1, sticky="W")
website_entry.focus()
username_entry = Entry(width=30)
username_entry.grid(column=1,row=2, sticky="W")
password_entry = Entry(width=30)
password_entry.grid(column=1,row=3, sticky="W")

# buttons
search_button = Button(text="Search",command=search_info,width=20)
search_button.grid(column=2,row=1, sticky="E")
generate_button = Button(text="Generate Password",command=generate_password,width=20)
generate_button.grid(column=2,row=3, sticky="E")
add_button = Button(text="Add",command=add_to_file,width=25)
add_button.grid(column=1,row=4, sticky="W")

screen.mainloop()