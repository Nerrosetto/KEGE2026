from turtle import *
m = 13
tracer(False)
lt(90)
screensize(3000,3000)
for i in range(2):
    fd(28*m)
    rt(90)
    fd(18*m)
    rt(90)
up()
fd(14*m)
rt(90)
fd(10*m)
rt(90)
down()
for i in range(2):
    fd(30*m)
    rt(90)
    fd(7*m)
    rt(90)
up()
for x in range(-40,40):
    for y in range(-40,40):
        goto(x*m,y*m)
        dot(3,'orange')
update()
done()