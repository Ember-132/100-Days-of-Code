from tkinter import *
import random
import json

# VARIABLES ------------------------>
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# FUNCTIONS ------------------------>
def new_word():
    '''Shows a new card/word. Triggered at start of program and when the user selects that they do not know a card'''
    global current_card
    # global flip_timer
    # window.after_cancel(flip_timer)

    # make sure the new card is not the same as the previous unless there is only one card remaining
    previous_card = current_card
    current_card = random.choice(list(data.items()))
    while current_card == previous_card and len(data)>1:
        current_card = random.choice(list(data.items()))

    # put the French word in the card
    canvas.itemconfig(canvas_image, image=front_of_card)
    canvas.itemconfig(language, text="French",fill="black")
    canvas.itemconfig(word,text=current_card[0],fill="black")
    # flip_timer = window.after(3000, func=flip_card)

def flip_card():
    '''flips the card over to show the answer'''
    # put the English word in the card
    canvas.itemconfig(canvas_image, image=back_of_card)
    canvas.itemconfig(language, text="English",fill="white")
    canvas.itemconfig(word, text=current_card[1],fill="white")

def is_known():
    '''If the user knows the word on the card, the button removes the card from the deck and checks if the deck is empty'''
    del data[current_card[0]]
    if len(data) == 0:
        canvas.itemconfig(canvas_image, image=front_of_card)
        canvas.itemconfig(word,text="You learnt the whole deck!",fill="black")
        canvas.itemconfig(language, text="")
        # once the deck is complete, exit the program after 2 seconds
        window.after(2000, window.destroy)
    else:
        new_word()

# UI ------------------------>
window = Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

# timer to flip card
# flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
back_of_card = PhotoImage(file="../day_31_flash-cards/images/card_back.png")
front_of_card = PhotoImage(file="../day_31_flash-cards/images/card_front.png")
canvas_image = canvas.create_image(400,263,image=front_of_card)
language = canvas.create_text(400,150,font=("Arial",26,"italic"))
word = canvas.create_text(400,263,font=("Arial",38,"bold"))
canvas.grid(column=1,row=0)

cross_image = PhotoImage(file="../day_31_flash-cards/images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=new_word)
unknown_button.grid(column=0,row=1)

reveal_button = Button(text="Flip",font=("Arial", 20, "normal"),highlightthickness=0,width=10,bg="azure",command=flip_card)
reveal_button.grid(column=1,row=1)

tick_image = PhotoImage(file="../day_31_flash-cards/images/correct.png")
known_button = Button(image=tick_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=is_known)
known_button.grid(column=2,row=1)

# MAIN CODE ------------------------>
# import the json data
with open("data/french_words.json", "r", encoding="utf-8") as word_data:
    data = json.load(word_data)
# select data with a random theme/topic
themes = [theme for theme in data]
chosen_theme = random.choice(themes)
data=data[chosen_theme]

new_word()

window.mainloop()