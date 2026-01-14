def f(x, y):
    return (x * y > A) or (x > y) or (11 > x)


for A in range(-1000, 1001)[::-1]:
    if all(f(x, y) for x in range(0, 1001) for y in range(0, 1001)):
        print(A)
        break
