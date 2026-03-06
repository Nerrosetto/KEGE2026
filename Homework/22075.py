def DIG(x, y):
    return str(x)[0] == str(y)[0]


def f(x, A):
    return DIG(x, 28) or (not DIG(x, 47)) or (x > A - 20)


ans = []
for A in range(1, 10000):
    if all(f(x, A) for x in range(1, 10000)):
        ans.append(A)
print(max(ans))
