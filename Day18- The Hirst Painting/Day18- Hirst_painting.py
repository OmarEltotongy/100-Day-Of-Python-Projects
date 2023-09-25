# import colorgram

# # Specify the path to the image file (e.g., 'image.jpg')
# image_path = 'f:\GitHub Repos\Projects of 100 Days of Python Programming\Day18- The Hirst Painting\image.jpg'

# colors = colorgram.extract(image_path, 6)
# my_tub = []

# for color in colors:
#     my_tub.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(my_tub)
import turtle
from turtle import Turtle as t
from turtle import Screen
import random

my_turt = t()

turtle.colormode(255)
color_list=[(239, 234, 226), (231, 238, 233), (232, 236, 241), (242, 233, 237), (186, 160, 139), (143, 166, 178)]
my_turt.penup()
my_turt.hideturtle()
my_turt.speed("fastest")
x_pose=-250
y_pose=-200
my_turt.setpos(x_pose,y_pose)

for _ in range (0,10):
    
    for _ in range(0,10):
        my_turt.pendown()
        my_turt.dot(20, random.choice(color_list))
        my_turt.penup()
        my_turt.forward(50)
    y_pose += 50
    my_turt.setpos(x_pose,y_pose)




screen = Screen()  
screen.exitonclick()