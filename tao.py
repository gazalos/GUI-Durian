# นี่คือโปรแกรมเต่าของฉัน

import turtle
tao = turtle.Pen()
tao.shape('turtle')

def Silium():
    print('กำลังวาดสี่เหลี่ยม')
    tao.forward(100)
    tao.left(90)
    tao.forward(100)
    tao.left(90)
    tao.forward(100)
    tao.left(90)
    tao.forward(100)
    tao.left(90)

def walking(x,y):
    print('กำลังเดินไปจ้า')
    tao.penup()
    tao.goto(x,y)
    tao.pendown()


def Randomwalking():
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    walking(x,y)
    Silium()

