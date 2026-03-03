from string import printable as pri

ans = set()
for y in pri[9:18]:
    for x in pri[0:pri.index(y)]:
        num1 = int(f'5{x}{y}A', 18)
        num2 = int(f'18{x}7', int(y, 18))
        num = num1 + num2
        ans |= {num}
print(len(ans))
