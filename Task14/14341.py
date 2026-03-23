from string import printable as pri

for x in range(22):
    num1 = int(f'56{x}{pri.index('c')}20', 22)
    num2 = int(f'89{pri.index('f')}{x}22', 22)
    num3 = int(f'{pri.index('h')}24{x}{pri.index('k')}21', 22)
    num = num1 + num2 + num3
    if num % 21 == 0:
        print(num // 21)
        break
