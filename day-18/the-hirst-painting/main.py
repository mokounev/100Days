import colorgram
import random
from turtle import Turtle, Screen
import turtle

# colors = colorgram.extract("hirst.jpg", 20)
# color_list = []
#
# for i in range(len(colors)):
#     r = colors[i].rgb.r
#     g = colors[i].rgb.g
#     b = colors[i].rgb.b
#     rgb = (r, g, b)
#
#     color_list.append(rgb)
#
# print(color_list)

### MASCHA'S SOLUTION
col_list = [(234, 229, 231), (236, 35, 108), (222, 231, 237), (145, 28, 65), (239, 74, 34), (6, 148, 93), (231, 238, 234), (232, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (172, 36, 98), (246, 219, 44), (42, 172, 112), (216, 130, 165), (216, 58, 26)]

t = Turtle()
turtle.colormode(255)
t.pu()
xpos = -250
ypos = -250
t.setpos(xpos, ypos)

for _ in range(10):
    t.setpos(xpos, ypos)
    for _ in range(10):
        t.color(random.choice(col_list))
        t.dot(20)
        t.pu()
        t.fd(50)
        ypos += 5


s = Screen()
s.exitonclick()
