def f(x, y, A):
    return (x ** 2 <= 136) or (y < 4 * x + A - 70) or (2 * y > 51)


for A in range(1, 9999):
    if all(f(x, y, A) for x in range(0, 1001) for y in range(0, 1001)):
        print(A)
        break
