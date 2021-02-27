#A pong game in Python

import turtle

wn = turtle.Screen() #creating window
wn.title("Pong") 
wn.bgcolor("blue")
wn.setup(width=800,height=600)
wn.tracer(0) #stops window from updating which speed up our game a bit

#score
score_a=0
score_b=0

#Paddle A
paddle_a = turtle.Turtle() #turtle object.  module name.class name
paddle_a.speed(0) #setting to max speed of the paddle animation
paddle_a.shape("square") #there are other shapes such as circles, triangles, etc
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #by default the .shape is 20 pixel by 20 pixel. we are stretching it
paddle_a.penup() #turtles draw line as they move. and this stop them from drawing line
paddle_a.goto(-350,0) #this is where the squre is going to start


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350,0)


#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

#devide ball movement in x and y
#SPEED of the ball!
ball.dx = .1  #delta x, change in direction x. Everytime the ball moves, it will move in .1
ball.dy = .1  #delta y, change in direction y


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


#functions
def paddle_a_up():
    y = paddle_a.ycor() #figure out the cordinate of the paddle_a
    y += 20 #going up
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20 #going down
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #figure out the cordinate of the paddle_a
    y += 20 #going up
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20 #going down
    paddle_b.sety(y)

#Keyboard binding
wn.listen() #window.listen listen for keyboard input
wn.onkeypress(paddle_a_up, "w") #call function paddle_a_up when lower case w is pressed
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    #check the border of the window
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #when the ball hits the top edge, it will change the direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0) #when the x edge is hit. send ball back to middle
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0) #when the x edge is hit. send ball back to middle
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1