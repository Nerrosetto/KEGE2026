def f(x, y):
    return (x < 7) or (y >= 5 * x + A - 60) or (x >= 36) or (y < 225)


ans = []
line_x = []
for A in range(1, 1001)[::-1]:
    if all(f(x, y) for x in range(1, 1001) for y in range(1, 1001)):
        print(A)
        break
