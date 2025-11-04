from turtle import *
screensize(3000, 3000)
lt(90)
m = 15
tracer(False)
for i in range(2):
    fd(5*m)
    lt(90)
    bk(13*m)
    lt(90)
up()
bk(10*m)
rt(90)
fd(9*m)
lt(90)
down()
for i in range(2):
    fd(11*m)
    rt(90)
    fd(7*m)
    rt(90)
up()
for x in range(-10, 40):
    for y in range(-40, 10):
        goto(x*m, y*m)
        dot(5, 'red')

update()
done()