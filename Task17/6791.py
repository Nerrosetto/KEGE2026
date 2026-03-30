with open(r'./Files/17_6791.txt') as file:
    data = [int(x) for x in file]
ans = []
mini = min([i for i in data if abs(i) % 100 == 68]) ** 2
for nums in zip(data, data[1:]):
    a = nums[0] ** 2 + nums[1] ** 2
    u1 = sum([abs(i) % 100 == 68 for i in nums]) == 1
    u2 = a >= mini
    if all((u1, u2)):
        ans.append(a)
print(len(ans), max(ans))
