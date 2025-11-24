from string import printable as al

for i in range(0,17):
    for x in al[:13]:
        numc = int(f'9{x}AB', 13)
    for x in al[:16]:
        numd = int(f'{x}46C', 16)
    for x in al[:15]:
        numee = int(f'B7{x}15', 15)
    num = numc + numd - numee
    if num % 14 == 0:
        print(x, num // 14)
