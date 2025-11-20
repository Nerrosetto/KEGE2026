a = 4 ** 36 + 3 * 4 ** 20 + 4 ** 15 + 2 * 4 ** 7 + 49
b = []
while a:
    b.append(a % 16)
    a //= 16
print(len(set(b)))
