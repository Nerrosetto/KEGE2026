def f(x):
    return (x & A == 0) <= ((x & 77 == 0) and (x & 44 == 0))


for A in range(1, 1001):
    if all(f(x) for x in range(1, 1001)):
        print(A)
        break
