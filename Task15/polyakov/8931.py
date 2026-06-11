def DEL(n, m):
    return n % m == 0


def F(x, A):
    return DEL(x, A) or ((2508 <= x <= 2570) <= ((not DEL(x, 214)) or (x + A <= 5286)))


ans = 0
for A in range(1, 3000)[::-1]:
    if all(F(x, A) for x in range(1, 3000)):
        ans = A
        break
print(ans)
