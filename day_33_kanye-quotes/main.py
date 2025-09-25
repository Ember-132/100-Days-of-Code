from tkinter import *
import requests

# FUNCTIONS ----->
def get_quote():
    '''get quote using API'''
    quote = requests.get(url="https://api.kanye.rest")
    quote.raise_for_status()
    data = quote.json()
    # display quote in speech bubble
    canvas.itemconfig(quote_text,text=data["quote"])

# UI ----->
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, width=250, font=("Arial", 22, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# MAIN CODE ----->
get_quote()

window.mainloop()