with open(r'C:\Users\Acer\PycharmProjects\KEGE20261\Task17\Files\17_1970.txt') as file:
    data = [int(x) for x in file]
ans = []
for num1, num2 in zip(data, data[1:]):
    u = any((num1 % 3 == 0, num2 % 3 == 0))
    if u:
        ans.append(num1 + num2)
print(len(ans), max(ans))
