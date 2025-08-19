from random import randint as RA

num = RA(0, 100)
if (num % 10) % 3 == 0:
    print(num // 3)
else:
    print(num * 2)
