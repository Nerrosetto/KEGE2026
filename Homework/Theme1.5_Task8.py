inp = int(input('Введите число: '))
n = 0
flag = False
while n < 11:
    if flag == True:
        break
    n += 1
    if inp % n != 0 and n != 10 and inp % 2 != 0 and inp % 3 != 0:
        flag = True
    else:
        pass
print(inp, 'это простое число.' if flag == True else 'это непростое число.')