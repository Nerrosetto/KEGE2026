from turtle import *
screensize(3000, 3000)
lt(90)
m = 12
tracer(False)
for i in range(2):
    fd(23*m)
    lt(90)
    bk(27*m)
    lt(90)
up()
bk(5*m)
rt(90)
fd(11*m)
lt(90)
down()
for i in range(2):
    fd(26*m)
    rt(90)
    fd(32*m)
    rt(90)
up()
for x in range(-25, 60):
    for y in range(-25, 40):
        goto(x*m, y*m)
        dot(5, 'red')

update()
done()