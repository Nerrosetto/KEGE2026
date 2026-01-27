# Системы счисления.

# Двоичная система.
N = 25
# bin() - переводит десятичное число в двоичную систему.
# Принимает на вход int, возвращает str.
# [2:] - срез, убирающий первые два символа '0b'.
print(bin(N)[2:])
# f'' - форматируемая строка, которая позволяет вставлять в себя переменные.
print(f'{N:b}')

# Восьмеричная система.
print(oct(N)[2:])
print(f'{N:o}')

# Шестнадцатеричная система.
print(hex(N)[2:])
print(f'{N:x}')


# Перевод в любую систему (2 <= sys <= 9) sys- system
def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'


print(convert(N, 3))

# Перевод в любую систему (2 <= sys <= 36)
from string import printable as al


def convert2(num, sys):
    res = ''
    while num != 0:
        res += al[num % sys]
        num //= sys
    return res[::-1]


# Перевод в десятичную систему.
num_bin = '101'
num_tri = '121'
num_hex = 'fa8'

print(int(num_bin, 2))
print(int(num_tri, 3))
print(int(num_hex, 16))

# Срезы.
data = "123456789"
# Извлечение первых двух символов.
print(data[:2])
# Извлечение без первых двух символов.
print(data[2:])
# Извлечение последних двух символов.
print(data[-2:])
# Извлечение без последних двух символов.
print(data[:-2])

# Сумма цифр числа.
# Двоичная система.
num1 = '1010'
sum1 = num1.count('1')

# Любая система до десятой включительно.
num2 = '193'
sum2 = sum(map(int, num2))
print(sum2)

a = [*map(int, num2)]
print(a)

# Любая система до 36 включительно.
num3 = 'AF5'
sum3 = sum(map(lambda x: int(x, 36), num3))
