with open(r'Files/17_28762.txt') as file:
    data = [int(i) for i in file]

ans = []
mini = min(i for i in data if i % 23 == 0)
for nums in zip(data, data[1:]):
    if sum([1 for i in nums if i % mini == 0]) >= 1:
        ans.append(sum(nums))
print(len(ans), max(ans))
