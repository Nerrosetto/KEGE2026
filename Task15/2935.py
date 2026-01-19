def f(x, y):
    return (2 * x + 3 * x != 135) or (y > A) or (x > A)


for A in range(-1000, 1001)[::-1]:
    if all(f(x, y) for x in range(0, 1001) for y in range(0, 1001)):
        print(A)
        break
