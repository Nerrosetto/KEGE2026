def f(x, y):
    return (x >= 11) or (3*x < y) or (x*y < A)


for A in range(1, 1001):
    if all(f(x, y) for x in range(1, 1001) for y in range(1, 1001)):
        print(A)
        break
