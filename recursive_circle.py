from turtle import *

from turtle import *

centerCircleSize = 300
minLength = centerCircleSize / 16
pencolor('orange')
fillcolor("orange")
speed(0)


def draw(x, y, length):
    penup()
    goto(x, y)
    pendown()

    begin_fill()
    dot(length)
    end_fill()

    if length > minLength:
        draw(x + length/2, y + length / 2, length / 2)  # draw the smaller square at the top-right corner
        draw(x + length/2, y - length/2, length / 2)  # draw the smaller square at the bottom-right corner
        draw(x - length / 2, y - length/2, length / 2)  # draw the smaller square at the bottom-left corner
        draw(x - length / 2, y + length / 2, length / 2)  # draw the smaller square at the top-left corner


draw(0, 0, centerCircleSize)

mainloop()
