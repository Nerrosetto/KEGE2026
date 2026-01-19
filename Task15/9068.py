def f(x, y):
    return (x >= 27) or (2*x < 3*y) or ((x+2)*(y-3) < A)


for A in range(1, 1001):
    if all(f(x, y) for x in range(1, 1001) for y in range(1, 1001)):
        print(A)
        break
