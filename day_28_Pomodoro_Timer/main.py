from tkinter import *
import math
import pygame

# ---------------------------- CONSTANTS AND VARIABLES ------------------------------- #
# Color pallette
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# Below 3 should all be 60
WORK_MIN = 60
SHORT_BREAK_MIN = 60
LONG_BREAK_MIN = 60

reps = 0
timer = None
current_min = None
current_sec = None
on = True
work_sec = WORK_MIN * 25
short_break_sec = SHORT_BREAK_MIN * 5
long_break_sec = LONG_BREAK_MIN * 15
allowed_change_stage=True
mark = ""

# ---------------------------- SOUND ------------------------------- #
pygame.mixer.init()
sound = pygame.mixer.Sound("long_alarm.wav")

# start playing the sound
def start_sound():
    sound.play()
    
# stop playing the sound
def stop_sound():
    sound.stop()

# ---------------------------- TIMER RESET ------------------------------- # 
def press_reset():
    '''When the reset button is pressed, the whole program reverts back to the initial state'''
    global timer
    global work_sec
    global short_break_sec
    global long_break_sec
    global mark
    global reps
    mark=""
    stop_sound()
    work_sec = WORK_MIN * 25
    short_break_sec = SHORT_BREAK_MIN * 5
    long_break_sec = LONG_BREAK_MIN * 15
    if timer is not None:
            try:
                window.after_cancel(timer)
            except Exception:
                pass
            timer = None
    timer_label.config(text="Timer")
    image.itemconfig(timer_text,text="00:00")
    tick.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_stop():
    '''Press to begin countdown and press again to pause. Timer works in order of Work, Short Break, Work,
    Short Break, Work, Long Break'''
    global reps
    global on
    global current_min
    global current_sec
    global work_sec
    global short_break_sec
    global long_break_sec
    global allowed_change_stage
    global timer

    # If the timer has finished, reset the countdown lengths
    if image.itemcget(timer_text, "text") == "00:00":
        if reps > 0:
            stop_sound()
        on=True
        work_sec = WORK_MIN * 25
        short_break_sec = SHORT_BREAK_MIN * 5
        long_break_sec = LONG_BREAK_MIN * 15
        allowed_change_stage = True
        reps+=1

    if on:
        # If countdown started
        on = False
        
        # Timer works in order of Work, Short Break, Work, Short Break, Work, Short Break, Work, Long Break
        if reps % 8 == 0:
            count_down(long_break_sec)
            if allowed_change_stage:
                timer_label.config(text="Long Break", fg=RED)
        elif reps % 2 == 0:
            count_down(short_break_sec)
            if allowed_change_stage:
                timer_label.config(text="Short Break", fg=PINK)
        else:
            count_down(work_sec)
            if allowed_change_stage:
                timer_label.config(text="Work", fg=RED)
    else:
        # If countdown stopped
        on = True
        allowed_change_stage = False
        
        # Store the current time when countdown is paused to pass it back into the countdown later
        if current_min is not None and current_sec is not None:
            remaining = (current_min * 60) + current_sec
            long_break_sec = remaining
            short_break_sec = remaining
            work_sec = remaining

        # Stop timer
        if timer is not None:
            try:
                window.after_cancel(timer)
            except Exception:
                pass
            timer = None

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    '''Counts down the timer in the correct format and triggers alarm when at 00:00'''
    global allowed_change_stage
    global current_min
    global current_sec
    global play_obj
    global timer
    global mark
    
    # Define length of a minute and a second and keep track of the current time
    count_min = math.floor(count/60)
    count_sec = count % 60
    current_min = count_min
    current_sec = count_sec

    # Fix the timer so that it displays as "00:00"
    display_min = f"{count_min:02}"
    display_sec = f"{count_sec:02}"
    image.itemconfig(timer_text,text=f"{display_min}:{display_sec}")

    # Count down by one second every second until time reaches 0
    if count>0:
        timer = window.after(1000, count_down, count-1)
    
    # When the timer reaches "00:00"
    else:
        start_sound()

        # Add a tick mark for every time a round of work has been completed
        if timer_label.cget("text") == "Work":
            mark += "✔"
            tick.config(text=mark)

        allowed_change_stage = True

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

# Label
timer_label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
timer_label.grid(column=1,row=0)

# Image and timer
image = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato_image.png")
image.create_image(100,112,image=tomato)
timer_text= image.create_text(100,125,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
image.grid(column=1,row=1)

# Start button
start_button = Button(text="Start/Stop",command=start_stop)
start_button.grid(column=0,row=2)

# Reset button
reset_button = Button(text="Reset",command=press_reset)
reset_button.grid(column=2,row=2)

# Tick marks
tick = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
tick.grid(column=1, row=3)

window.mainloop()