from random import randint

num = randint(0, 100)

print(num // 3 if num % 3 == 0 else num * 2)
