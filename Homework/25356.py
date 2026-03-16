with open(r'C:\Users\Acer\PycharmProjects\KEGE20261\Task17\Files\17_25356.txt') as file:
    data = [int(x) for x in file]
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    num1, num2, num3 = str(num1), str(num2), str(num3)
    u1 = all((len(num1) != 4, len(num2) != 4, len(num3) != 4))
    li = []
    for i in (num1, num2, num3):
        if i[-2] == '30':
            li.append(int(i))
    u2 = sum(map(int, (num1, num2, num3))) > 9930
    if all((u1, u2)):
        ans.append(sum(map(int, (num1, num2, num3))))
print(len(ans), max(ans))

# Не работает.