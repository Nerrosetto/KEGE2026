from turtle import *

screensize(250,250)
tracer(False)
m = 5

for i in range(3):
    fd(19*m)
    rt(90)
    fd(30*m)
    rt(90)
up()
fd(2*m)
rt(90)
fd(8*m)
lt(90)
down()
for i in range(4):
    fd(93*m)
    rt(90)
    fd(97*m)
    rt(90)

up()
for x in range(-90, 31):
    for y in range(-30, 90):
        goto(x*m, y*m)
        dot(3, 'orange')

update()
done()