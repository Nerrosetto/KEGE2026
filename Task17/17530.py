with open(r'C:\Users\Acer\PycharmProjects\KEGE20261\Task17\Files\17_17530.txt') as file:
    data = [int(x) for x in file]
ans = []
mini = min(data)
for nums in zip(data, data[1:]):
    u = any((nums[0] % 55 == mini, nums[1] % 55 == mini))
    if u:
        ans.append(sum(nums))
print(len(ans), min(ans))
