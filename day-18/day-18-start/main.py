from turtle import Turtle, Screen
import random
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("coral")


# Draw a square
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# Draw a dashed line
tim = Turtle()

# for _ in range(10):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
directions = [0, 90, 180, 270]

for _ in range(100):
    tim.speed("fastest")
    tim.color(random.choice(colours))
    tim.setheading(random.choice(directions))
    tim.pensize(8)
    tim.forward(30)


# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(360 / num_sides)
#
#
# for i in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(i)


# for _ in range(3):
#     tim.forward(100)
#     tim.right(120)
#
# tim.color("brown")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# tim.color("brown1")
# for _ in range(5):
#     tim.forward(100)
#     tim.right(72)
#
# tim.color("chocolate1")
# for _ in range(6):
#     tim.forward(100)
#     tim.right(60)
#
# tim.color("chocolate4")
# for _ in range(7):
#     tim.forward(100)
#     tim.right(360/7)
#
# tim.color("DarkOrange")
# for _ in range(8):
#     tim.forward(100)
#     tim.right(45)
#
# tim.color("DarkOrange4")
# for _ in range(9):
#     tim.forward(100)
#     tim.right(40)
#
# tim.color("DarkRed")
# for _ in range(10):
#     tim.forward(100)
#     tim.right(36)

screen = Screen()
screen.exitonclick()
