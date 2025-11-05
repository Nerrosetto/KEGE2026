from turtle import *

screensize(1024,1024)
tracer(False)
m = 8
lt(90)
for x in range(4):
    fd(30*m)
    rt(90)
    fd(48*m)
    rt(90)
up()
fd(27*m)
rt(90)
fd(24*m)
lt(90)
down()
for x in range(4):
    fd(29*m)
    rt(90)
    bk(18*m)
    rt(90)
up()
for x in range(-15, 60):
    for y in range(-10, 60):
        goto(x*m, y*m)
        dot(3, 'orange')

update()
done()