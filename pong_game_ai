import turtle
import random
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
speed = [0.38,0.4,0.42]
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
scoreboard.write(f'P1 : {score_a}   AI : {score_b}', align='center', font=('Courier', 24, 'normal'))

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


#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")



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
        ball.dx = random.choice(speed)* -1
        ball.dy = random.choice(speed)
        score_a += 1
        scoreboard.clear()
        scoreboard.write(f'P1 : {score_a}   AI : {score_b}', align='center', font=('Courier', 24, 'normal'))
    elif ball.xcor() <-400:
        ball.goto(0,0)
        ball.dx = random.choice(speed)
        ball.dy = random.choice(speed) * -1
        score_b += 1
        scoreboard.clear()
        scoreboard.write(f'P1 : {score_a}   AI : {score_b}', align='center', font=('Courier', 24, 'normal'))

    #paddle and ball collision
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+15 and ball.ycor()>paddle_a.ycor()-15):
        ball.dx = random.choice(speed) * 1.5
        ball.dy = 0

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()>paddle_a.ycor()+15 and ball.ycor()<paddle_a.ycor()+60):
        ball.dx = random.choice(speed)
        ball.dy = random.choice(speed)

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()-15 and ball.ycor()>paddle_a.ycor()-60):
        ball.dx = random.choice(speed)
        ball.dy = random.choice(speed) * -1

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+15 and ball.ycor()>paddle_b.ycor()-15):
        ball.dx = random.choice(speed) * -1.5
        ball.dy = 0

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()>paddle_b.ycor()+15 and ball.ycor()<paddle_b.ycor()+60):
        ball.dx = random.choice(speed) * -1
        ball.dy = random.choice(speed)

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()-15 and ball.ycor()>paddle_b.ycor()-60):
        ball.dx = random.choice(speed) * -1
        ball.dy = random.choice(speed) * -1

    #AI
    if  ((ball.ycor() > paddle_b.ycor() + random.randint(50,500)) and ball.dx > 0) and (random.randint(0,100)>50):
        paddle_b.sety(paddle_b.ycor() + 10)

    if  ((ball.ycor() < paddle_b.ycor() - random.randint(50,500))) and ball.dx > 0 and (random.randint(0,100)>50):
        paddle_b.sety(paddle_b.ycor() - 10)

    if (ball.dx<0 and paddle_b.ycor()<0) and (random.randint(0,100)>95):
        paddle_b.sety(paddle_b.ycor() + 10)

    if (ball.dx<0 and paddle_b.ycor()>0) and (random.randint(0,100)>95):
        paddle_b.sety(paddle_b.ycor() - 10)



    if score_a==3:
        print('Player win!')
        messagebox.showinfo("Congratulations!", "You win!")
        break

    if score_b==3:
        print('Computer win!')
        messagebox.showinfo("Pity!", "You lose!")
        break
