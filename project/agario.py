
import turtle
import time
import random
from ball import Ball
import math


turtle.tracer(0)
turtle.hideturtle()
writer=turtle.clone()
writer1=turtle.clone()

RUNNING=True
ALIVE = True
SLEEP=0.0077
SCREEN_WIDTH=int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT=int(turtle.getcanvas().winfo_height()/2)

turtle.color("black")
turtle.write("Eat smaller balls to get bigger. If you want to quit, just press the space bar", font = ("Ariel", 12), align="center")
time.sleep(2)
turtle.clear()

MY_BALL=Ball(2,2,1,1,20,"cyan2")

NUMBERS_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=30
MINIMUM_BALL_DX=-2
MAXIMUM_BALL_DX=2
MINIMUM_BALL_DY=-2
MAXIMUM_BALL_DY=2

SPACEBAR="space"
def quitgame():
    turtle.bye()
turtle.onkeypress(quitgame,"space")
turtle.listen()

score=0

balls=[]
for i in range(NUMBERS_OF_BALLS):
    x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
    y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
    dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
    while(dx == 0 and dy ==0):
        dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
        dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
    radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
    color=(random.random(), random.random(), random.random())
    ball=Ball(x,y,dx,dy,radius,color)
    balls.append(ball)


for i in balls:
    i.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball1,ball2):
    if ball1==ball2:
        return False
    d = math.sqrt(math.pow((ball2.xcor()-ball1.xcor()),2) + math.pow((ball2.ycor()-ball1.ycor()),2))
    if (d+10)<=ball1.r+ball2.r:
        return True
    else:
        return False

def check_collision():
    for balla in balls:
        for ballb in balls:
            if collide(balla,ballb):
                new_x = random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
                new_y = random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
                new_dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                new_dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                while(new_dx == 0 and new_dy ==0):
                    dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                    dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                new_r = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                new_color = (random.random(), random.random(), random.random())
                
                if balla.r>ballb.r:
                    ballb.goto(new_x, new_y)
                    ballb.dx=new_dx
                    ballb.dy=new_dy
                    ballb.r=new_r
                    ballb.color(new_color, new_color)
                    ballb.shapesize(ballb.r/10)
                    balla.r+= 5
                    balla.shapesize(balla.r/10)
                elif ballb.r>balla.r:
                    balla.goto(new_x, new_y)
                    balla.dx=new_dx
                    balla.dy=new_dy
                    balla.r=new_r
                    balla.color(new_color, new_color)
                    balla.shapesize(balla.r/10)
                    ballb.r+= 5
                    ballb.shapesize(ballb.r/10)


def check_myball_collision():
    for balla in balls:
            if collide(MY_BALL,balla)==True:
                new_x = random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
                new_y = random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
                if balla.r>MY_BALL.r:
                    return False
                elif MY_BALL.r>balla.r:
                    global score
                    MY_BALL.r+=5
                    MY_BALL.shapesize(MY_BALL.r/10)
                    balla.goto(new_x, new_y)
                    balla.dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                    balla.dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                    while(balla.dx == 0 and balla.dy ==0):
                        dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                        dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                    balla.r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                    balla.color(random.random(), random.random(), random.random())
                    balla.shapesize(balla.r/10)
                    score=score+1
                    print(score)
    return True

def movearound(event):
    MY_BALL.goto(event.x-SCREEN_WIDTH,SCREEN_HEIGHT-event.y)

turtle.getcanvas().bind("<Motion>",movearound)
turtle.getscreen().listen()

writer.penup()
writer.goto(50,-250)

level = 1
    
while RUNNING:
    if SCREEN_WIDTH!=int(turtle.getcanvas().winfo_width()/2) or SCREEN_HEIGHT!=int(turtle.getcanvas().winfo_height()/2):
        SCREEN_WIDTH=int(turtle.getcanvas().winfo_width()/2)
        SCREEN_HEIGHT=int(turtle.getcanvas().winfo_height()/2)

    writer.clear()
    writer.write("your score is "+str(score), font=("Arial", 17, "normal"))
    if  MY_BALL.r>SCREEN_WIDTH:
        writer1.write("You won! In next level all the other balls will move faster!", font=("Arial",17, "normal"),align="center")
        time.sleep(3)
        writer1.clear()
        MY_BALL.goto(0,0)
        MY_BALL.dx=1
        MY_BALL.dy=1
        MY_BALL.r=20
        MY_BALL.color("cyan")
        MY_BALL.shapesize(MY_BALL.r/10)
        level+=1
        MINIMUM_BALL_DX*= level
        MAXIMUM_BALL_DX*= level
        MINIMUM_BALL_DY*= level
        MAXIMUM_BALL_DY*= level
        
    for i in balls:
        i.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    check_collision()
    #MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    RUNNING = check_myball_collision()
    turtle.update()
    time.sleep(SLEEP)


turtle.write("Game Over", font=("Arial", 42, "normal"),align="center")
time.sleep(2)
quitgame()
turtle.mainloop()
