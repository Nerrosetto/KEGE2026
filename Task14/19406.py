from string import printable as al

for x in al[1:35]:
    res = []
    num1 = int(f'6{x}QR{x}', 35)
    num2 = int(f'{x}59SH', 35)
    num3 = int(f'PH{x}69YW', 35)
    num = num1 + num2 + num3
    num = str(num)
    for i in num:
        res.append([num.count(i), i])
    a = max(res)[1]
    if int(num) % int(a) ** 2 == 0:
        print(x, int(num) // int(a) ** 2)
