with open(r'C:\Users\Acer\PycharmProjects\KEGE20261\Task17\Files\17_9840.txt') as file:
    data = [int(x) for x in file]
ans = []
max_39 = max(abs(i) for i in data if i % 100 == 39 and len(str(abs(i))) == 4)
for nums in zip(data, data[1:]):
    u1 = sum([1 for i in nums if len(str(abs(i))) == 4]) == 1
    u2 = sum(nums) ** 2 <= max_39 ** 2
    if u1 and u2:
        ans.append(sum(nums))
print(len(ans), max(ans))
