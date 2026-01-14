def f(x, y):
    return (2 * x + y != 110) or (x < y) or (A < x)


for A in range(-1001, 1001)[::-1]:
    if all(f(x, y) for x in range(0, 1001) for y in range(0, 1001)):
        print(A)
        break
