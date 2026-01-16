def f(x):
    B = 70 <= x <= 90
    return (x % A == 0) or (B <= (x % 22 != 0))


for A in range(1, 1001)[::-1]:
    if all(f(x) for x in range(1, 1001)):
        print(A)
        break
