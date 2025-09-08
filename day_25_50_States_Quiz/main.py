import turtle
import pandas
from writing import Writing

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

writer = Writing()
continuing = True

#READ THE FILE TO GET CURRENT SCORE
with open("record.csv", mode="r") as record:
    current_score = int(record.read())

data = pandas.read_csv("50_states.csv")
all_states= data["state"].tolist()

missing_dict = {
      "States_to_learn": all_states

  }
reset_to_learn = pandas.DataFrame(missing_dict)

missing = pandas.read_csv("to_learn.csv")
missing_states= missing["States_to_learn"].tolist()

while continuing:

    writer.write_instruction()  
    guessed = pandas.read_csv("states_learnt.csv")
    guessed_states= guessed["states"].tolist()

    # ITERATE THROUGH THE GUESSED STATE LIST AND WRITE ON BOARD ANY STATES ALREADY GUESSED IN OLDER GAMES
    for state in guessed_states:
        row = data[data.state == state]
        x = row.x.item()
        y = row.y.item()
        writer.write_state(state, x, y)

    screen.update()
    #PROMPT THE USER TO GUESS A STATE
    answer_state = screen.textinput(title=f"{current_score}/50 States correct", prompt="Enter a State: ").title()
    
    #GAME WILL CLOSE IF USER TYPES 'EXIT'
    if answer_state == "Exit":
        continuing = False
    # GAME WILL RESET IF USER TYPES 'RESET'
    elif answer_state == "Reset":

        current_score = 0
        with open("record.csv", mode ="w") as reset_score:
            reset_score.write(f"{current_score}")
            reset_score.close()

        reset_to_learn.to_csv("to_learn.csv")

        with open("states_learnt.csv", mode ="w") as reset_guessed:
            reset_guessed.write(f",states")
            reset_score.close()

        writer.clear_screen()

    #IF THE USER GUESS IS PRESENT IN THE MISSING STATES LIST, INCREASE N.O CORRECT ANSWERS AND ADD TO GUESSED LIST
    elif answer_state in missing_states:
        current_score += 1
        missing = missing.drop(missing[missing.States_to_learn == answer_state].index)
        missing.to_csv('to_learn.csv', index=False)

        new_row = pandas.DataFrame({'states': [answer_state]})
        guessed = pandas.concat([guessed,new_row], ignore_index=True)
        guessed.to_csv('states_learnt.csv', index=False)

        with open("record.csv", mode ="w") as file:
            file.write(f"{current_score}")
            file.close()

        if current_score == 50:
            continuing = False
        else:
            answer_state_row = data[data.state == answer_state]
            answer_state_x = answer_state_row.x.item()
            answer_state_y = answer_state_row.y.item()

            writer.write_state(answer_state,answer_state_x,answer_state_y)

screen.exitonclick()
