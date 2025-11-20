a = 16 ** 820 - 2 ** 761 + 14
b = 0
while a:
    if a % 4 == 0:
        b += 1
    a //= 4
print(b)
