import turtle

print("Press Tab to start the game")
print("Controls : a key for left, d key for right")
Lives = 3

#Screen
window = turtle.Screen()
window.bgcolor("Blue")
window.title("4k graphics")
window.setup(width=800, height=500)
window.tracer(0)

#Creating paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("yellow")
paddle.shapesize(
    stretch_len=3,
    stretch_wid=0.5)  #Length = 60 pixels, Width = 10 pixels (1 = 20 pixels)
paddle.penup()
paddle.goto(0, -220)

#Creating enemy
enemy = turtle.Turtle()
enemy.speed(0)
enemy.shape("square")
enemy.color("black")
enemy.shapesize(
    stretch_len=6,
    stretch_wid=0.5)  #Length = 120 pixels, Width = 10 pixels (1 = 20 pixels)
enemy.penup()
enemy.goto(0, 220)
enemy.dx = 1

#Score display
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 0)
score.write("Lives : {}".format(Lives),
            align="center",
            font=("Courier", 10, "normal"))

#Score display
display = turtle.Turtle()
display.speed(0)
display.color("white")
display.penup()
display.hideturtle()
display.goto(0, 0)

#Creating dummy bullet
bullet = turtle.Turtle()
bullet.dy = 0
bullet.penup()
bullet.goto(1000, 1000)


#Defining bullet
def spawn_bullet():
    global bullet
    bullet = turtle.Turtle()
    bullet.speed(0)
    bullet.shape("square")
    bullet.color("red")
    bullet.shapesize(stretch_len=0.5, stretch_wid=0.5
                     )  #Height = 10 pixels, Width = 10 pixels (1 = 20 pixels)
    bullet.penup()
    bullet.goto(enemy.xcor(), enemy.ycor())
    bullet.dx = 0.5
    bullet.dy = 0.5


#Defining cmd to move paddle
def paddle_right():
    x = paddle.xcor()
    x += 5
    paddle.setx(x)


def paddle_left():
    x = paddle.xcor()
    x -= 5
    paddle.setx(x)


#Key binding
window.listen()
window.onkeypress(spawn_bullet, "Tab")

window.listen()
window.onkeypress(paddle_right, "d")

window.listen()
window.onkeypress(paddle_left, "a")

#Loop
while True:
    window.update()

    while enemy.xcor() < paddle.xcor():  #Enemy following paddle
        enemy.setx(enemy.xcor() + enemy.dx)

    while enemy.xcor() > paddle.xcor():  #Enemy following paddle
        enemy.setx(enemy.xcor() - enemy.dx)
    if Lives > 0:
        bullet.sety(bullet.ycor() - bullet.dy)

    if bullet.ycor() - 10 == paddle.ycor() + 10 and bullet.xcor(
    ) > paddle.xcor() - 30 and bullet.xcor(
    ) < paddle.xcor() + 30:  #Detecting paddle
        Lives -= 1
        bullet.goto(enemy.xcor(), enemy.ycor())
        score.clear()
        score.write("Lives : {}".format(Lives),
                    align="center",
                    font=("Courier", 10, "normal"))

    elif Lives == 0:
        bullet.goto(10000, 10000)
        paddle.goto(0, 10000)
        enemy.goto(0,-10000)
        display.write("You ded!",
                      align="center",
                      font=("Courier", 40, "normal"))

    elif bullet.ycor() == -250:  #Making bullet go back to enemy
        bullet.goto(enemy.xcor(), enemy.ycor())

    elif paddle.xcor() + 30 > 400:
        paddle.goto(370, -220)

    elif paddle.xcor() - 30 < -400:
        paddle.goto(-370, -220)