from string import printable as pri

ans = []
for x in pri[:7]:
    for y in pri[:7]:
        a = f'{y}{x}320'
        b = f'1{x}3{y}3'
        if a[0] != '0':
            num = int(a, 7) + int(b, 9)
            if num % 181 == 0:
                ans.append(num // 181)
print(min(ans))
