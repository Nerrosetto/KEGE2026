from string import printable as al


def convert(num, sys):
    a = ''
    while num:
        a += al[num % sys]
        num //= sys
    return a[::-1]


for x in al[:100]:
    num1 = convert(f'7A{x}0123', 100)
    num2 = convert(f'1BA64{x}', 100)
    num3 = convert(f'{x}98012C', 100)
    num = num1 - num2 + num3
    if num % 21 == 0:
        print(x, convert(num, 6))
