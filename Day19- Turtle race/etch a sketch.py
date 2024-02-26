import turtle
from turtle import Turtle as t
from turtle import Screen

my_turt = t()

screen = Screen()

def move_fwd():
    my_turt.forward(10)
def move_bwd():
    my_turt.backward(10)
def rotate_CW():
    my_turt.left(10)
def rotate_CCW():
    my_turt.right(10)
def clear_Dwg():
    my_turt.home()
    my_turt.clear()
    
    
screen.listen()
screen.onkey(key="w",fun=move_fwd)
screen.onkey(key="s",fun=move_bwd)
screen.onkey(key="a",fun=rotate_CW)
screen.onkey(key="d",fun=rotate_CCW)
screen.onkey(key="c",fun=clear_Dwg)

screen.exitonclick()

