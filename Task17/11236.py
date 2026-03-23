with open(r'C:\Users\Acer\PycharmProjects\KEGE20261\Task17\Files\17_11236.txt') as file:
    data = [int(i) for i in file]
maxx = max(i for i in data if 1000 <= abs(i) <= 9999 and abs(i) % 10 == 1)
mino = min(i for i in data if 10 <= abs(i) <= 99) ** 2
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = mino < num1
    u2 = mino < num2
    u3 = mino < num3
    u4 = abs(num1 * num2 * num3) % maxx == 0
    if all((u1 + u2 + u3 == 2, u4)):
        ans.append(sum(map(abs, [num1, num2, num3])))
print(len(ans), max(ans))
