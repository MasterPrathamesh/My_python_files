import turtle
col = ['yellow', 'red', 'green', 'orange', 'blue', 'white']

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed(30)

count = 0
i = 0

for i in range(120):
    t.color(col[i%6])
    t.forward(i*4)
    t.left(150)
    t.width(2)