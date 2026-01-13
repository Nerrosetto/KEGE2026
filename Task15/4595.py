def f(x):
    return ((x % 2 == 0) <= (not (x % 3 == 0))) or (x + A >= 80)


for A in range(1, 1001):
    if all(f(x) for x in range(1, 1001)):
        print(A)
        break
