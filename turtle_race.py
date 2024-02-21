import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
race_ongoing = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
winning_turtle = None
x = -230
y = -75

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x, y)
    all_turtles.append(new_turtle)
    y += 30

if user_bet:
    race_ongoing = True

while race_ongoing:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 240:
            print(turtle, turtle.color())
            race_ongoing = False
            winning_turtle = turtle.color()[0]

if winning_turtle == user_bet:
    print(f"You won the bet! Winner: {winning_turtle}")
else:
    print(f"You lost the bet. Winner: {winning_turtle}")

screen.exitonclick()
