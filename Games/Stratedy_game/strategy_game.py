import turtle
import time
import random

#Defining variables
army = 1
interest = 1
time_survived = 0
territory = 1000
available_territory = 98000
b_army, b_interest, b_territory = army, interest, territory
continuing = True
won = None
lost = None

#Screen
window = turtle.Screen()
window.bgcolor("Black")
window.title("You should be studying rn")
window.setup(width=800, height=400)
window.tracer(0)

#Display of army, etc.
info_screen = turtle.Turtle()
info_screen.speed(0)
info_screen.color("white")
info_screen.penup()
info_screen.hideturtle()
info_screen.goto(0, 150)

#Display of various msgs
news_screen = turtle.Turtle()
news_screen.speed(0)
news_screen.color("white")
news_screen.penup()
news_screen.hideturtle()
news_screen.goto(0, -160)

#Bot's stats display
bot_stats = turtle.Turtle()
bot_stats.speed(0)
bot_stats.color("white")
bot_stats.penup()
bot_stats.hideturtle()
bot_stats.goto(0, 100)


#Defining cmds
#Player's expand cmd
def expand():
    global territory, army, available_territory
    if available_territory > 0:
        percent = int(input("Enter percentage of your army to spend"))
        if percent >= 1 and percent <= 100:
            territory += (percent * army) / 100
            territory = round(territory)
            army -= (percent * army) / 100
            available_territory -= territory
            army, territory, available_territory = round(army), round(
                territory), round(available_territory)
        else:
            print("Please try again and type numbers between 1 and 100")


#Player's attack cmd
def attack():
    global b_territory, b_army, territory, army, won
    percent = int(input("Enter percentage of your army to spend"))
    if percent >= 1 and percent <= 100:
        army_per = (percent * army) / 100
        b_army -= army_per / 2
        b_territory -= army_per / 2
        army -= army_per
        territory += army_per / 2
        b_army, b_territory, army, territory = round(b_army), round(
            b_territory), round(army), round(territory)
        if b_territory <= 0 or b_army <= 0:
            won = True
            print("You Won")
    else:
        print("Please try again and type numbers between 1 and 100")


#Bot's expand cmd
def b_expand():
    global b_territory, b_army, available_territory
    if available_territory > 0:
        for n in range(1, 99):
            if b_army - (b_army * n) / 100 >= army:
                b_percent = n
            else:
                b_percent = random.randint(1, 5)
        b_territory += (b_percent * b_army) / 100
        b_territory = round(b_territory)
        b_army -= (b_percent * b_army) / 100
        available_territory -= b_territory
        b_army, b_territory, available_territory = round(b_army), round(
            b_territory), round(available_territory)


#Bot's attack cmd
def b_attack():
    global b_territory, b_army, territory, army, lost
    if b_army / 2 >= army or b_army / 2 >= territory:
        percent = 100
    else:
        percent = random.randint(1, 10)
    b_army_per = (percent * b_army) / 100
    army -= b_army_per / 2
    territory -= b_army_per / 2
    b_army -= b_army_per
    b_territory += b_army_per / 2
    b_army, b_territory, army, territory = round(b_army), round(
        b_territory), round(army), round(territory)
    if territory <= 0 or army <= 0:
        lost = True
        print("You Lost")


#Key binding
window.listen()
window.onkeypress(expand, "e")

window.listen()
window.onkeypress(attack, "a")

#Loop
while continuing == True:

    army += interest
    army = round(army)

    time_survived += 1

    interest = territory / (time_survived * 1.5)
    interest = round(interest)

    b_army += b_interest
    b_army = round(b_army)

    b_interest = b_territory / (time_survived * 1.5)
    b_interest = round(b_interest)

    #Bot's decisions
    decision = random.randint(1, 5)
    if decision == 1:
        print("Bot expanded!")
        b_expand()
    elif decision == 2:
        print("Bot attacked you!")
        b_attack()
    elif decision > 3:
        None

    info_screen.clear()
    info_screen.write(
        "Army : {} ; Territory : {} ; Increase rate : {} ; Time survived : {} ; available_territory : {}"
        .format(army, territory, interest, time_survived, available_territory),
        align="center",
        font=("Courier", 9, "normal"))

    bot_stats.clear()
    bot_stats.write(
        "BOT'S STATS - Army : {} ; Territory : {} ; Increase rate : {}".format(
            b_army, b_territory, b_interest),
        align="center",
        font=("Courier", 9, "normal"))

    if won == True or lost == True:
        continuing = False

    time.sleep(1)
