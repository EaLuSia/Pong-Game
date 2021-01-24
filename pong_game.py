import turtle
from tkinter import messagebox
wn=turtle.Screen()
wn.title('ping-pong')
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(5,1)
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(5,1)
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx=0.15
ball.dy=-0.15

#score
score_a = 0
score_b = 0

#scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color('white')
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write(f'P1 : {score_a}   P2 : {score_b}', align='center', font=('Courier', 24, 'normal'))

#function
def paddle_a_up():
    y = paddle_a.ycor()
    if y>=300:
        paddle_a.sety(y)
    else:
        y += 20
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y<=-300:
        paddle_a.sety(y)
    else:
        y -= 20
        paddle_a.sety(y)


def paddle_b_up(event):
    y = paddle_b.ycor()
    if y>=300:
        paddle_b.sety(y)
    else:
        y += 20
        paddle_b.sety(y)


def paddle_b_down(event):
    y = paddle_b.ycor()
    if y<=-300:
        paddle_b.sety(y)
    else:
        y -= 20
        paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")

wn.listen()
wn.getcanvas().bind('<Up>',paddle_b_up)
wn.getcanvas().bind('<Down>',paddle_b_down)

#main game loop
while score_a<3 and score_b<3:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor()>290:
        ball.dy *= -1
    elif ball.ycor() < -280:
        ball.dy *= -1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        scoreboard.clear()
        scoreboard.write(f'P1 : {score_a}   P2 : {score_b}', align='center', font=('Courier', 24, 'normal'))
    elif ball.xcor() <-400:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        scoreboard.clear()
        scoreboard.write(f'P1 : {score_a}   P2 : {score_b}', align='center', font=('Courier', 24, 'normal'))

    #paddle and ball collision
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50):
        ball.dx *= -1

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50):
        ball.dx *= -1

    if score_a==3:
        print('Player1 win!')
        messagebox.showinfo("Congratulations!", "Player1 win!")
        break

    if score_b==3:
        print('Player2 win!')
        messagebox.showinfo("Congratulations!", "Player2 win!")
        break
