import turtle
import time
import random
try:
    window=turtle.Screen()
    window.title("Snake Game")
    window.bgcolor("green")
    window.setup(width=600,height=600)
    window.tracer(0)
    head=turtle.Turtle()
    head.speed(0)
    head.shape("circle")
    head.color("red")
    head.penup()
    head.goto(0,0)
    head.direction="stop"
    food=turtle.Turtle()
    food.speed(0)
    food.shape("square")
    food.color("grey")
    food.penup()
    food.goto(0,100)

    score=0
    high_score=0
    body=[]
    text=turtle.Turtle()
    text.speed(0)
    text.shape("square")
    text.color("white")
    text.penup()
    text.hideturtle()
    text.goto(0,260)
    text.write("Score : 0    High score : 0",align="center",font=("Courier",24,"normal"))
    def go_up():
        if head.direction!="down":
            head.direction="up"
    def go_down():
        if head.direction!="up":
            head.direction="down"
    def go_left():
        if head.direction!="right":
            head.direction="left"
    def go_right():
        if head.direction!="left":
            head.direction="right"

    def move():
        if head.direction=="up":
            y=head.ycor()
            head.sety(y+10)
        if head.direction=="down":
            y=head.ycor()
            head.sety(y-10)
        if head.direction=="left":
            x=head.xcor()
            head.setx(x-10)
        if head.direction=="right":
            x=head.xcor()
            head.setx(x+10)
    window.listen()
    window.onkeypress(go_up,"Up")
    window.onkeypress(go_down,"Down")
    window.onkeypress(go_left,"Left")
    window.onkeypress(go_right,"Right")

    while True:
        window.update()
        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for j in body:
                j.goto(1000,1000)

            body.clear()
            score=0
            text.clear()
            text.write("Score : {}    High score : {}".format(score,high_score),align="center",font=("Courier",24,"normal"))

        if head.distance(food)<20:
            x=random.randint(-290,290)
            y=random.randint(-290,290)
            food.goto(x,y)

            add_body=turtle.Turtle()
            add_body.speed(0)
            add_body.shape("circle")
            add_body.color("red")
            add_body.penup()
            body.append(add_body)

            score+=5
            if score>high_score:
                high_score=score
            text.clear()
            text.write("Score : {}    High score : {}".format(score,high_score),align="center",font=("Courier",24,"normal"))

        for i in range(len(body)-1,0,-1):
            x=body[i-1].xcor()
            y=body[i-1].ycor()
            body[i].goto(x,y)
        if len(body)>0:
            x=head.xcor()
            y=head.ycor()
            body[0].goto(x,y)

        move()
    
        for a in body:
            if a.distance(head) < 10:
                time.sleep(1)
            
                head.goto(0,0)
                head.direction="stop"
                for b in body:
                    b.goto(1000,1000)
            
                body.clear()
                score=0
                text.clear()
                text.write("Score : {}    High score : {}".format(score,high_score),align="center",font=("Courier",24,"normal"))
                break
            
        time.sleep(0.1)
    



    window.mainloop()
except:
    print("work is done")
