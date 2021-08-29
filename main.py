# import colorgram
#
# colors = colorgram.extract("image.jpg",30)
#
# color_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tuple_color = (r, g, b)
#     color_list.append(tuple_color)
# print(color_list)


import turtle as turtle_module
from turtle import Screen
import random

turtle_module.colormode(255)
color_list = [(199, 13, 32), (250, 237, 18), (39, 76, 189), (39, 217, 69), (229, 159, 46), (237, 226, 5), (28, 40, 156), (214, 75, 13), (197, 15, 11), (16, 154, 15), (242, 35, 165), (229, 17, 121), (70, 10, 31), (240, 244, 251), (61, 15, 8), (224, 141, 209), (11, 97, 62), (222, 160, 9), (52, 212, 230), (18, 19, 43), (11, 227, 238), (238, 156, 217), (85, 74, 209), (79, 210, 159), (89, 233, 197), (60, 232, 241), (4, 68, 42)]


tim = turtle_module.Turtle()
tim.setheading(225)
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.forward(250)
tim.setheading(0)


x_num = 8
y_num = 8
for y in range(y_num):
    for x in range(x_num):
        color_random = random.choice(color_list)
        tim.pendown()
        tim.dot(20, color_random)
        tim.penup()
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(50*(x_num))
    tim.setheading(0)



screen = Screen()
screen.exitonclick()