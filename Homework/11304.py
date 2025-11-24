from string import printable as al

for x in al[:16]:
    numa = int(f'11{x}73', 16)
    numb = int(f'94662{x}53{x}', 16)
    numc = int(f'6{x}41', 16)
    numd = int(f'31{x}77', 16)
    numee = int(f'9{x}82{x}{x}181', 16)
    num = numa + numb + numc + numd + numee
    if num % 15 == 0:
        print(x, num // 15)
