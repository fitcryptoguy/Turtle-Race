import time
from turtle import Turtle, Screen
import random
from random import randint

# create 5 diff Turtle class objects
turtle_list = []
for i in range(5):
    turtle_list.append(Turtle())

# screen setup
screen = Screen()
screen.setup(700, 500)

user_bet = screen.textinput(title="Make your bet beba", prompt="which turtle you want to select: ")

dimension = [-100, 100, -50, 50, 0]
color = ["red", "green", "yellow", "black", "blue"]

# setting turtle color and size
for i in range(5):
    turtle_list[i].penup()
    turtle_list[i].goto(-320, dimension[i])
    turtle_list[i].shape("turtle")
    turtle_list[i].pensize(4)
    turtle_list[i].color(color[i])
    turtle_list[i].forward(30)

# starting the race
game_on = True
while game_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won {winning_color}")

            else:
                print("you loose")
                print(f"color won {winning_color}")
            game_on = False
        random_num = randint(0, 10)
        turtle.forward(random_num)


screen.exitonclick()
