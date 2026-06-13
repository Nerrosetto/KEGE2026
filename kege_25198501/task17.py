with open(r'../kege_25198501/files/17_17558.txt') as file:
    data = [int(i) for i in file]

cnt = 0
maxi = -1 * 2 ** 100
u2 = len([i for i in data if i % 32 == 0])
for nums in zip(data, data[1:]):
    if sorted(abs(i) for i in nums) != sorted(nums):
        if sum(nums) < u2:
            cnt += 1
            maxi = max(sum(nums), maxi)
print(cnt, maxi)
