# Visual Stimulation 1 - Spin Syntax (Spyntax)
"""
A captivating rainbow "pinwheel" that uses concentric shapes. Each adorned with the vibrant colors of the rainbow to create a stimulative display.

"""
import turtle
# Set the screen size and background colors
screen = turtle.Screen()
screen.setup(width=1400, height=1400)
screen.bgcolor('black')

rainbow_pen = turtle.Turtle()
rainbow_pen.pensize(4) 
rainbow_pen.speed(10) 
colors = ["red", "orange", "yellow", "green", "blue", "blueviolet", "violet"]

for i in range(300):
    rainbow_pen.pencolor(colors[i % len(colors)])
    rainbow_pen.stamp()
    rainbow_pen.forward(i*2)
    rainbow_pen.left(116)
    rainbow_pen.backward(i*4)
    rainbow_pen.left(64)
    rainbow_pen.forward(i*1)
    rainbow_pen.left(117)

turtle.done()