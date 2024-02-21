from turtle import Turtle, Screen, colormode
from random import choice, randint
import colorgram

turtle = Turtle()

screen = Screen()
screen.colormode(255)

## Shape drawing tri-dec

# for i in range(3, 11):
#     turtle.color(randint(0, 255),
#                  randint(0, 255),
#                  randint(0, 255))
#     for j in range(i):
#         turtle.forward(100)
#         turtle.right(360 / i)


## Random walk\
# turtle.speed("fastest")
# directions = [0, 90, 180, 270]
# for i in range(1000):
#     turtle.color(randint(0, 255),
#                  randint(0, 255),
#                  randint(0, 255))
#     turtle.width(10)
#     turtle.forward(20)
#     turtle.setheading(choice(directions))


## Spirograph
# turtle.speed("fastest")
# for i in range(36):
#     turtle.color(randint(0, 255),
#                  randint(0, 255),
#                  randint(0, 255))
#     turtle.circle(100)
#     turtle.right(10)


## Hirst Dot Painting
# turtle.speed("fastest")
# colors = colorgram.extract('painting.jpg', 10)
# rgb_tuples = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_tuples.append([r, g, b])
#
# print(rgb_tuples)
#
# rgb_colors = [[199, 175, 117], [124, 36, 24], [210, 221, 213], [168, 106, 57], [186, 158, 53], [6, 57, 83], [109, 67, 85]]
# def hirst_painting(width):
#     turtle.penup()
#     # determines the size of the board based on width where width is # of dots across
#     # this is actually determining half the size of the board for positioning reasons
#     turtle_position = int(width * 25)
#     x = -turtle_position - 25
#     y = -turtle_position + 25
#
#     for i in range(width):
#         turtle.setpos(x, y)
#         for j in range(width):
#             turtle.color(choice(rgb_colors))
#             turtle.forward(50)
#             turtle.dot(20)
#         y += 50
#
#     print(turtle.pos())
#
# hirst_painting(10)


## Etch a sketch
#
# def move_forwards():
#     turtle.forward(10)
#
#
# def move_backwards():
#     turtle.backward(10)
#
#
# def turn_right():
#     turtle.right(10)
#
#
# def turn_left():
#     turtle.left(10)
#
#
# def clear():
#     turtle.up()
#     turtle.home()
#     turtle.clear()
#     turtle.down()
#
#
# screen.listen()
# screen.onkey(fun=move_forwards, key="Up")
# screen.onkey(fun=move_backwards, key="Down")
# screen.onkey(fun=turn_left, key="Left")
# screen.onkey(fun=turn_right, key="Right")
# screen.onkey(fun=clear, key="c")

screen.exitonclick()
