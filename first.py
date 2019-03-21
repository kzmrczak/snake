import turtle
import time
import random

width = 600
height = 600

# setup screen
w = turtle.Screen()
w.title("Snake")
w.bgcolor("white")
w.setup(width=width, height=height)
w.tracer(0)

delay = 0.07

# body

partsOfBody = []

# head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"
step = 20


# apple
x = random.randrange(-width/2+20, width/2-20, step)
y = random.randrange(-height/2+20, height/2-20, step)

ap = turtle.Turtle()
ap.speed(0)
ap.shape("circle")
ap.color("red")
ap.penup()
ap.goto(x,y)


def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():


    if head.direction == "up":
        head.sety(head.ycor() + step)
    elif head.direction == "down":
        head.sety(head.ycor() - step)
    elif head.direction == "left":
        head.setx(head.xcor() - step)
    elif head.direction == "right":
        head.setx(head.xcor() + step)
    else:
        head.direction = "stop"

    if head.ycor() > height/2:
        head.sety(-height/2)
    if head.ycor() < -height/2:
        head.sety(height/2)

    if head.xcor() > width/2:
        head.setx(-width/2)
    if head.xcor() < -width/2:
        head.setx(width/2)


def death():
    time.sleep(1)
    for parts in partsOfBody:
        parts.goto(800,800)
    partsOfBody.clear()
    head.goto(0, 0)
    head.direction = "stop"

w.listen()
w.onkeypress(go_up, "w")
w.onkeypress(go_down, "s")
w.onkeypress(go_left, "a")
w.onkeypress(go_right, "d")

while True:
    w.update()

    if head.distance(ap) < 20:
        x = random.randrange(-width / 2 + 20, width / 2 - 20, step)
        y = random.randrange(-height / 2 + 20, height / 2 - 20, step)
        ap.goto(x, y)
        #delay -= 0.001
        newPart = turtle.Turtle()
        newPart.speed(0)
        newPart.shape("square")
        newPart.color("yellow")
        newPart.fillcolor("orange")
        newPart.penup()
        partsOfBody.append(newPart)


    for i in range(len(partsOfBody) - 1,0,-1):
        bx = partsOfBody[i - 1].xcor()
        by = partsOfBody[i - 1].ycor()
        partsOfBody[i].goto(bx, by)



    if len(partsOfBody) > 0:
        bx = head.xcor()
        by = head.ycor()
        partsOfBody[0].goto(bx, by)

    move()

    for i in partsOfBody:
        if i.distance(head) < 20:
            death()


    print(partsOfBody)
    time.sleep(delay)



w.mainloop()

