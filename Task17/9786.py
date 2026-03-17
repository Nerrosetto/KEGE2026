with open(r'C:\Users\Acer\PycharmProjects\KEGE20261\Task17\Files\17_9786.txt') as file:
    data = [int(x) for x in file]
ans = []
max_25 = max(i for i in data if abs(i) % 100 == 25)
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    a = [num1, num2, num3]
    cnt = sum((True for i in (num1, num2, num3) if len(str(abs(i))) == 4)) <= 2
    uB = sum(map(int, a)) < max_25
    if cnt and uB:
        ans.append(sum(map(int, a)))
print(len(ans), max(ans))
