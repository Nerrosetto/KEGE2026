def DEL(n, m):
    return n % m == 0


def F(x, A):
    return DEL(x, 21) <= ((not DEL(x, A)) <= (not DEL(x, 77)))


ans = 0
for A in range(1, 4000)[::-1]:
    if all(F(x, A) for x in range(1, 3000)):
        ans = A
        break
print(ans)
