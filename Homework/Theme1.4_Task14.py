inp = int(input('Введите трёхзначное число: '))
flag = 0
if (inp // 100) % 5 == 0 or (inp // 100) % 2 == 0:
    flag += 1
if (inp // 10 % 10) % 5 == 0 or (inp // 10 % 10) % 2 == 0:
    flag += 1
if (inp % 10) % 5 == 0 or (inp % 10) % 2 == 0:
    flag += 1
if flag >= 2:
    print(inp)
else:
    print(inp + 1)