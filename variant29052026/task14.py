from string import printable as pri

for x in pri[:29]:
    num1 = int(f'463{x}7921', 29)
    num2 = int(f'8241{x}153', 29)
    if (num1 + num2) % 28 == 0:
        print((num1 + num2) // 28)
        break
