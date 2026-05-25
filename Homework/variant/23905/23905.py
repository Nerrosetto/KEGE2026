with open(r'17_23905.txt') as file:
    data = [int(i) for i in file]

a = max(i for i in data if i % 100 == 37)
ans = []
for num in zip(data, data[1:], data[2:], data[3:]):
    if len([i for i in num if abs(i) % 100 == 37]):
        u2 = len([i > a for i in sorted(num, reverse=True)[:2]]) == 2
        if u2:
            u3_step1 = [str(i) for i in num]
            u3_step2 = sum([1 for i in u3_step1 if len(str(i[-2:])) == 1]) == 1
            if u3_step2:
                ans.append(sum(num))
print(len(ans), sum(ans))
