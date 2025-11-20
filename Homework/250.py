res = []
for a in range(1, 40):
    f = a
    b = ""
    while f:
        b += str(f % 2)
        f //= 2
    c = b[::-1]
    if c[-4:] == '1011':
        res.append(a)
print(max(res))
