def f(x, y, A):
    return (2 * x + y != 110) or (x < y) or (A < x)


for A in range(1, 3000)[::-1]:
    if all(f(x, y, A) for x in range(1,3000), y in range(1, 3000)):
        print(A)
        break
