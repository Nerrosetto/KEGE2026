from random import random

Num1 = random()
Num2 = int(Num1 * 10000)
Num3 = Num2 % 10
Num4 = Num2 // 1000
Num5 = Num2 // 100 % 10
Num6 = Num2 // 10 % 10
print(Num4 + Num5 + Num6 + Num3)
