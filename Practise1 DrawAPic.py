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
        t.pen(pencolor=((r*i,g,b)),fillcolor=((r*i,g,b)),speed=100)
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
drawaSun(100,-100,"yellow",'yellow',0)
#Draw 15 Trees
for i in range(15):
    x = random.randint(-400,400)
    y = random.randint(-700,-450)
    size = random.randint(50,150)
    drawaTree(x,y,size,10,"orange",0,i*10,0)
for i in range(10):
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    size = random.randint(5,10)
    drawaBird(x,y,"brown","black",size)

turtle.done()

