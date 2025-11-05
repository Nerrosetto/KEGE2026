from turtle import *

screensize(250,250)
tracer(False)
m = 8
lt(90)
rt(270)
for i in range(2):
    fd(8*m)
    rt(120)
rt(120)
for i in range(2):
    rt(120)
    fd(3*m)
    rt(240)
rt(240)
for i in range(2):
    fd(14*m)
    rt(120)
up()
for x in range(-15, 30):
    for y in range(-15, 30):
        goto(x*m, y*m)
        dot(3, 'orange')

update()
done()