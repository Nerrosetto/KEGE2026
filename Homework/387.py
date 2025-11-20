a = 51 * 7 ** 12 - 7 ** 3 - 22
b = 0
while a:
    b += a % 7
    a //= 7
print(b)
