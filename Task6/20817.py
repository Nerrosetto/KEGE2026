from turtle import *
m = 13
tracer(False)
lt(90)
screensize(3000,3000)
for i in range(2):
    fd(27*m)
    rt(90)
    fd(12*m)
    rt(90)
up()
fd(4*m)
rt(90)
fd(6*m)
lt(90)
down()
for i in range(2):
    fd(83*m)
    rt(90)
    fd(77*m)
    rt(90)
up()
for x in range(-40,40):
    for y in range(-40,40):
        goto(x*m,y*m)
        dot(3,'orange')
update()
done()