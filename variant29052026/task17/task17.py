with open(r'17_23276.txt') as file:
    data = [int(i) for i in file]

for_u2 = max(i for i in data if abs(i) % 100 == 25)
cnt = 0
maxi = 0
for nums in zip(data, data[1:], data[2:]):
    if [len(str(abs(i))) for i in nums].count(4) <= 2:
        if sum(nums) <= for_u2:
            cnt += 1
            maxi = max(sum(nums), maxi)
print(cnt, maxi)
