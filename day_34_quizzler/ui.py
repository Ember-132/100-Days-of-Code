from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Interface:
    '''The UI for the quiz'''
    def __init__(self, quiz_brain:QuizBrain):
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.quiz = quiz_brain

        self.score = Label(text=f"Score: {self.quiz.score}",bg=THEME_COLOR,fg="white")
        self.score.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.text = self.canvas.create_text(150,125,text="demo",font=("Arial",15,"italic"),width=275)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)

        tick_image = PhotoImage(file="images/true.png")
        self.tick = Button(image=tick_image,command=self.tick_pressed)
        self.tick.grid(row=2,column=0)

        cross_image = PhotoImage(file="images/false.png")
        self.cross = Button(image=cross_image,command=self.cross_pressed)
        self.cross.grid(row=2, column=1)

        self.show_next_question()


        self.window.mainloop()

    def show_next_question(self):
        '''Shows the next question if there are any not yet asked, otherwise shows and end of game message with score'''
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_txt = self.quiz.next_question()
            self.canvas.itemconfig(self.text,text=q_txt)
        else:
            self.canvas.itemconfig(self.text, text=f"END OF GAME\nYou scored {self.quiz.score}/10")
            self.tick.config(state="disabled")
            self.cross.config(state="disabled")

    def tick_pressed(self):
        self.change_display(self.quiz.check_answer("true"))

    def cross_pressed(self):
        self.change_display(self.quiz.check_answer("false"))

    def change_display(self,is_correct:bool):
        '''If the user answers a question correctly the screen flashes green, or if incorrect it flashes red'''
        if is_correct:
            self.canvas.config(bg="green")
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.show_next_question)

