import turtle

screen = turtle.Screen()
screen.title('Pin Pon')
screen.setup(width=600, height=600)
screen.bgcolor('light blue')
screen.tracer(0)

player = turtle.Turtle()
player.speed(0)
player.shape('square')
player.color('black')
player.penup()
player.goto(0, -250)
player.shapesize(1, 5)

ball = turtle.Turtle()
ball.speed(10)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.dx = 0.30
ball.dy = 0.30

def player_right():
    x = player.xcor()
    x = x + 18
    player.setx(x)
def player_left():
    x = player.xcor()
    x = x - 18
    player.setx(x)

screen.listen()
screen.onkeypress(player_left, 'Left')
screen.onkeypress(player_right, 'Right')



while True:
    screen.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
   

    if ball.xcor()>290 or ball.xcor()<-290:
        ball.dx = ball.dx * -1
    
    if ball.ycor()>290:
        ball.dy = ball.dy * -1
        

    if ball.ycor()>390:
        ball.goto(0, 0)
        ball.dy = ball.dy * -1
        
    if ball.ycor()<-390:
        ball.goto(0, 0)
        ball.dy = ball.dy * -1
        
    if (ball.ycor()<-240 and ball.ycor()>-250) and (ball.xcor()<player.xcor()+60 and ball.xcor()>player.xcor()-60):
        ball.sety(-240)
        ball.dy = ball.dy * -1
        
        