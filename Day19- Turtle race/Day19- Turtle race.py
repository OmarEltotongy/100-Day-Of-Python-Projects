from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(height=400, width=500)
user_guess = screen.textinput(
    title="Guess the Winner", prompt="Do u think who will win ?")

red_tur = Turtle(shape="turtle")
orange_tur = Turtle(shape="turtle")
yellow_tur = Turtle(shape="turtle")
green_tur = Turtle(shape="turtle")
blue_tur = Turtle(shape="turtle")
purple_tur = Turtle(shape="turtle")

all_turt = [red_tur, orange_tur, yellow_tur, green_tur, blue_tur, purple_tur]

is_the_race_on = False

red_tur.penup()
red_tur.fillcolor("red")
orange_tur.penup()
orange_tur.fillcolor("orange")
yellow_tur.penup()
yellow_tur.fillcolor("yellow")
green_tur.penup()
green_tur.fillcolor("green")
blue_tur.penup()
blue_tur.fillcolor("blue")
purple_tur.penup()
purple_tur.fillcolor("purple")

red_tur.goto(-240, -100)
orange_tur.goto(-240, 100)
yellow_tur.goto(-240, -150)
green_tur .goto(-240, 150)
blue_tur.goto(-240, -50)
purple_tur.goto(-240, 50)

is_the_race_on = True

while is_the_race_on:

    for turtle in all_turt:
        if (turtle.xcor() > 230):
            is_the_race_on = False
            wining_turtle = turtle.fillcolor()
            if (user_guess == wining_turtle):
                print(" Yes thats right, WINNER")
            else:
                print(f"No thats wrong, Lost.\nThe correct one is {
                      wining_turtle}")

    for turtle in all_turt:
        turtle.forward(random.randint(0, 15))


screen.exitonclick()
