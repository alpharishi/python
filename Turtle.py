import turtle

tina = turtle.Turtle()
tina.shape('turtle')

tina.left(90)
tina.forward(20)
tina.write("What color am I now?")

tina.forward(20)
tina.color("blue")
tina.write("What color am I now?")

tina.forward(20)
tina.color("purple")
tina.write("What color am I now?")

tina.forward(20)
tina.color("black")
tina.write("What color am I now?")

tina.penup()
tina.write("I start at 0, 0")

tina.goto(200,200)
tina.write("This is 200, 200")

tina.goto(-200,-200)
tina.write("This is -200, -200")

tina.goto(200,-200)
tina.write("This is 200, -200")

tina.goto(-200,200)
tina.write("This is -200, 200")

tina.goto(-200, 0)

turtle.done()


