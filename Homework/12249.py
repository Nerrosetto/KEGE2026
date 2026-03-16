with open(r'C:\Users\Acer\PycharmProjects\KEGE20261\Task17\Files\17_12249.txt') as file:
    data = [int(x) for x in file]
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    num1, num2, num3 = str(num1), str(num2), str(num3)
    u1 = any((num1[-1] == '3', num2[-1] == '3', num3[-1] == '3'))
    u2 = sum(map(int, (num1, num2, num3))) <= 99993
    if all((u1, u2)):
        ans.append(sum(map(int, (num1, num2, num3))))
print(len(ans), max(ans))
