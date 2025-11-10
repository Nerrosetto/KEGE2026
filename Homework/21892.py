from turtle import *

screensize(1024,1024)
tracer(False)
m = 14
lt(90)
rt(90)
for i in range(7):
    rt(45)
    fd(11*m)
    rt(45)

up()
for x in range(-10, 10):
    for y in range(-20, 5):
        goto(x*m, y*m)
        dot(5, 'orange')

update()
done()
