from turtle import *

screensize(250,250)
tracer(False)
m = 5

for i in range(3):
    fd(22*m)
    rt(90)
    fd(6*m)
    rt(90)
up()
fd(1*m)
rt(90)
fd(5*m)
lt(90)
down()
for i in range(4):
    fd(53*m)
    rt(90)
    fd(75*m)
    rt(90)

up()
for x in range(-90, 30):
    for y in range(-30, 90):
        goto(x*m, y*m)
        dot(3, 'orange')

update()
done()