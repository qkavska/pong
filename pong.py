import turtle

# window
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# pad1
pad1 = turtle.Turtle()
pad1.speed(0)
pad1.shape("square")
pad1.color("white")
pad1.shapesize(stretch_wid=8, stretch_len=1)
pad1.penup()
pad1.goto(-350, 0)

# pad2
pad2 = turtle.Turtle()
pad2.speed(0)
pad2.shape("square")
pad2.color("white")
pad2.shapesize(stretch_wid=8, stretch_len=1)
pad2.penup()
pad2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

# functions
def pad1_up():
    y = pad1.ycor()
    y += 20
    pad1.sety(y)

def pad1_down():
    y = pad1.ycor()
    y -= 20
    pad1.sety(y)

def pad2_up():
    y = pad2.ycor()
    y += 20
    pad2.sety(y)

def pad2_down():
    y = pad2.ycor()
    y -= 20
    pad2.sety(y)

wn.listen()
wn.onkeypress(pad1_up, "w")
wn.onkeypress(pad1_down, "s")
wn.onkeypress(pad2_up, "Up")
wn.onkeypress(pad2_down, "Down")


while True:
    wn.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad2.ycor() + 40 and ball.ycor() > pad2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pad1.ycor() + 40 and ball.ycor() > pad1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

