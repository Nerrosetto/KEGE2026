def f(x, y, A):
    return (x > A) or (y > A) or (x + 2 * y < 80)


for A in range(0, 3000)[::-1]:
    if all(f(x, y, A) for x in range(1, 2000) for y in range(1, 2000)):
        print(A)
        break
