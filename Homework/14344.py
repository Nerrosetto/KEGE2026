from string import printable as al

for p in range(16, 37):
    numa = int(f'17496', p)
    numb = int(f'91F83', p)
    numc = int(f'D9543', p)
    num = numa + numb + numc
    if num % 12 == 0:
        print(p, num // 12)