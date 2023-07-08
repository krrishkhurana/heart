import turtle
pen=turtle.Turtle()
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)
def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(111)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
def txt():
    pen.up(50)
    pen.speed(90)
    pen.down(-60)
    pen.color('black')
    pen.write("KHURANA",font=("verdana",12,"bold"))
heart()
txt()
pen.ht()
