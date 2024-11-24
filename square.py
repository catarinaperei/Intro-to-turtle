import turtle
turtle.Screen().bgcolor("purple")
turtle.Screen().setup(400,300)

star=turtle.Turtle()
for i in range(4):
    star.forward(100)
    star.right(90)

turtle.done()