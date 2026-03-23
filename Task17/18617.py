with open(r'C:\Users\Acer\PycharmProjects\KEGE20261\Task17\Files\17_18617.txt') as file:
    data = [int(t) for t in file]
maxi = max(i for i in data) % 3
mini = min(i for i in data) % 7
ans = []
for nums in zip(data, data[1:]):
    u1 = sum((i % 3 == maxi) for i in nums) >= 1
    u2 = sum((i % 7 == mini) for i in nums) >= 1
    if all((u1, u2)):
        ans.append(sum(nums))
print(len(ans), max(ans))
