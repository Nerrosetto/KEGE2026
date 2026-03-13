from turtle import *

m = 10
screensize(3000, 3000)
tracer(False)
lt(90)
for i in range(4):
    fd(7 * m)
    lt(90)
    fd(7 * m)
    lt(90)
    fd(7 * m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(5, 'orange')
update()
done()
