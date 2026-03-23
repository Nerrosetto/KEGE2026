with open(r'C:\Users\Acer\PycharmProjects\KEGE20261\Task17\Files\17_5758.txt') as file:
    data = [int(i) for i in file]
moda = max((data.count(i), i) for i in set(data))[1]
ans = []
for i in range(len(data)):
    for j in range(i + 2, len(data), 2):
        if min(data[i], data[j]) < moda < max(data[i], data[j]):
            ans += [max((abs(data[i] - moda), abs(data[j] - moda)))]
print(len(ans), max(ans))
