from turtle import *

tracer(False)
screensize(3000, 3000)
left(90)
k = 20
x = 2
down()
for i in range(4):
    forward(x * k)
    right(90)
    forward(x * k)
    left(90)
    forward(x * k)
    right(90)
up()
for i in range(0, 3 * x + 1):
    for y in range(-x, 2 * x + 1):
        goto(i * k, y * k)
        dot()
update()
done()
