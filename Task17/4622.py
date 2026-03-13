with open(r'.\Files\17_4622.txt') as file:
    data = [int(x) for x in file]
# min_19 = min([i for i in data if i > 0 and i % 19 == 0])
min_19 = min(i for i in data if i > 0 and i % 19 == 0)

ans = []
for num1, num2 in zip(data, data[1:]):
    u = int(num1) + num2 < min_19
    if u:
        ans.append(num1 + num2)
print(len(ans), max(ans))
