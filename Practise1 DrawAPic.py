#gdgffdg This is the third time change# Drawing a Picture
from turtle import *
import turtle
import random
from turtle import Screen
screen = Screen()
screen.colormode(255)
screen.bgcolor("Orange")
t = turtle.Turtle()

def setbgcolor(y,r,g,b):
    for i in range(50):
        t.penup()
        t.goto(-370,y)
        t.pendown()
        t.seth(0)
        t.begin_fill()
        t.pen(pencolor=((r*i,g,b)),fillcolor=((r*i,g,b)),speed=1000)
        #t.fillcolor((r*i,g,b))
        print(r*i)
        t.fd(800)
        t.lt(90)
        t.fd(15)
        t.lt(90)
        t.fd(800)
        t.lt(90)
        t.fd(15)
        t.end_fill()
        y += 15
        

def drawaSun(x,y,pcolor,fcolor,psize):
    t = turtle.Turtle()
    t.penup()
    t.goto(x,y)
    t.seth(0)
    t.pendown()
    t.pen(pencolor=pcolor,fillcolor=fcolor,pensize=psize,speed=100)
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.penup()


def drawaBird(x,y,outline,fillcolor,size):
    t.up()
    t.goto(x,y)
    t.seth(0)
    t.down()
    t.pen(pencolor=outline,fillcolor=fillcolor,pensize=size/8,speed=100)
    t.penup
    t.begin_fill()
    t.circle(size,90)
    t.rt(60)
    t.fd(size)
    t.lt(160)
    
    t.fd(size)
    t.rt(90)
    t.circle(size,200)
    #paint the body of the bird
    t.rt(120)
    t.circle(5*size,60)
    #paint the tail
    t.rt(60)
    t.fd(5*size)
    for i in range(6):
        t.circle(size/3,180)
        t.rt(160)
    t.lt(90)
    t.fd(4*size)
    t.rt(90)
    t.circle(5*size,120)
    t.lt(95)
    t.fd(5*size)
    t.end_fill()

def drawaTree(x,y,size,psize,ocolor,r,g,b):
    t.penup()
    t.goto(x,y)
    t.seth(0)
    t.begin_fill()
    t.pen(pencolor=ocolor,fillcolor=((r,g,b)),pensize=psize/12,speed=100)
    t.lt(90)
    t.fd(400)
    t.lt(140)
    for i in range(8):
        t.circle(-size,60)
        t.rt(160)
        t.circle(size,60)
        t.lt(120)
    t.fd(400)
    t.rt(90)
    t.fd(size/4)
    t.rt(90)
    t.rt(size+psize)
    t.end_fill()
#draw a cat to add to the scene
t = turtle.Turtle()
def drawaCat(a,b,size,outline,fillcolor,scolor1,scolor2):
    # body
    t.penup()
    t.goto(a,b-1.6*size)
    t.seth(0)
    t.pendown()
    t.begin_fill()
    t.pen(pencolor=outline,fillcolor=fillcolor,pensize=size/50,speed=50)
    t.circle(size)
    t.penup()
    t.end_fill()

    # head
    t.penup()
    t.goto(a,b)
    t.pen(pencolor=outline,fillcolor=fillcolor,pensize=size/50,speed=50)
    t.pendown()
    t.begin_fill()
    t.circle(size*0.6)
    t.penup()
    t.end_fill()

    # Eyes
    t.penup()
    t.goto(a-int(abs(size/5)),b+int(abs(size/1.5)))
    t.pendown()
    t.begin_fill()
    t.color("yellow")
    t.circle(size/20)
    t.penup()
    t.end_fill()
    t.penup()
    t.goto(a+int(abs(size/5)),b+int(abs(size/1.5)))
    t.pendown()
    t.begin_fill()
    t.color("black")
    t.circle(size/20)
    t.penup()
    t.end_fill()


    #Whiskers
    for i in range(4):
        t.penup()
        t.goto(a-int(abs(size/5)),b+int(abs(size/2)))
        t.pen(pencolor="black",pensize=size/50,speed=5)
        t.pendown()
        t.seth(160)
        t.lt(15*i)
        t.fd(size/2)

        # t.goto(a-21,b+24)
    for i in range(4):
        t.penup()
        t.goto(a+int(abs(size/5)),b+int(abs(size/2)))
        t.pen(pencolor=scolor2,pensize=size/50,speed=5)
        t.pendown()
        t.seth(20)
        t.rt(15*i)
        t.fd(size/2)

    #Ears
    t.penup()
    t.goto(a,b)
    t.goto(a-int(abs(size/2)),b+int(abs(size*0.7)))
    t.pen(pencolor=fillcolor,pensize=size/50,speed=5)
    t.begin_fill()
    t.seth(45)
    t.pendown()
    for i in range (3):
        t.fd(size/2)
        t.lt(120)
    t.end_fill()
    
    t.penup()
    t.goto(a+int(abs(size/2)),b+int(abs(size*0.7)))
    t.begin_fill()
    t.pen(pencolor=fillcolor,pensize=size/50,speed=5)
    t.seth(60)
    t.pendown()
    for i in range (3):
        t.fd(size/2)
        t.lt(120)
    t.end_fill()
        
    #Tail
    t.penup()
    t.goto(a,b-int(abs(size)))
    t.pendown()
    t.pen(pencolor=fillcolor,pensize=size/10,speed=5)
    t.seth(0)
    t.circle(size,90)
    t.seth(90)
    t.circle(-size,90)
    t.penup()
#Main drawing process
t.penup()
setbgcolor(-350,4,40,80)
#Draw 30 stars
for i in range(30):
    x = random.randint(-400,400)
    y = random.randint(100,400)
    size = random.randint(3,8)
    t.penup()
    t.goto(x,y)
    t.pencolor("yellow")
    t.dot(size)
    t.pendown()

drawaSun(200,200,"yellow",'yellow',0)

#Draw 5 Trees and 5 Birds
for i in range(7):
    x = random.randint(-400,400)
    y = random.randint(-700,-350)
    size = random.randint(50,150)
    drawaTree(x,y,size,10,"orange",0,i*30,0)
for i in range(7):
    x = random.randint(-300,300)
    y = random.randint(-100,300)
    size = random.randint(5,10)
    drawaBird(x,y,"yellow","white",size)

drawaCat(0,-230,80,"black","grey","black","pink")
drawaCat(100,-300,40,"black","grey","black","pink")

turtle.done()

