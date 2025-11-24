from string import printable as al

for x in al[:27]:
    numa = int(f'8{x}38{x}68', 27)
    numb = int(f'37{x}3163', 27)
    num = numa + numb
    if num % 26 == 0:
        print(x, num // 26)
