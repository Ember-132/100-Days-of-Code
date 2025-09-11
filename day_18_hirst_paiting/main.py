# import colorgram
#
#
# Get the colors from the image
#
# color_list = []
# number_of_colors = 21
# colors = colorgram.extract('hirst_image.jpg',number_of_colors)
# for n in colors:
#     r = n.rgb.r
#     g = n.rgb.g
#     b = n.rgb.b
#     new_color = (r,g,b)
#     color_list.append(new_color)
#
# print(color_list)

import turtle as t
import random

# define colors created from the previous colorgram extraction
colour_list =[(236, 35, 108), (221, 231, 237), (145, 28, 66), (230, 237, 232), (239, 75, 35), (7, 148, 95), (220, 171, 45), (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91), (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35), (239, 162, 193)]

# create the turtle/pen
tim = t.Turtle()
tim.penup()
t.colormode(255)
tim.hideturtle()
dots = 0
vertical_location = -200
tim.teleport(0,vertical_location)

# draw 100 dots with random colors from the list
while dots < 100:
    if dots % 10 == 0:
        new_y_location = vertical_location + 50
        tim.goto(0,new_y_location)
        vertical_location = new_y_location
    tim.dot(20,random.choice(colour_list))
    tim.forward(50)
    dots +=1


t.exitonclick()