def f(x, y):
    B = 70 <= x <= 90
    return x % A or (B <= (not x % 22))


for A in range(-1000, 1001)[::-1]:
    if all(f(x, y) for x in range(1, 1001) for y in range(1, 1001)):
        print(A)
        break
