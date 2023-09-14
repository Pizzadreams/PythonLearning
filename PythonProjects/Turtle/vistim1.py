# Visual Stimulation 1
import turtle
# Set the screen size and background color
screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor('black')

turtle.color('cyan')

#turtle.pensize(1)

turtle.speed(0.1)

for i in range(900):
    turtle.stamp()
    turtle.forward(i*2)
    turtle.left(117)
    turtle.backward(i*5)
    turtle.left(64)
    turtle.forward(i*2)
    turtle.left(117)



turtle.done()