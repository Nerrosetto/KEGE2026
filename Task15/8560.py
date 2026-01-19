def f(x, y, z):
    return (2*x + y != 136) or (z*y) < 100 or (A**2 >= x+y)


for A in range(1, 1001):
    if all(f(x, y, z) for x in range(1, 1001) for y in range(1, 1001) for z in range(1, 1001)):
        print(A)
        break
