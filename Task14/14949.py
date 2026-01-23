from string import printable as pri

for x in pri[1:8]:
    numa = int(f'{x}1{x}', 16)
    numb = int(f'{x}3{x}3', 8)
    num = numa + numb
    for i in range(1, 300):
        if 2 ** i == num:
            print(x)
