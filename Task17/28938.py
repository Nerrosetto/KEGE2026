with open(r'Files/17_28938.txt') as file:
    data = [int(i) for i in file]

ans = []
maxi = max(i for i in data if abs(i) % 100 == 28)
for nums in zip(data, data[1:], data[2:]):
    if sum([1 for i in nums if len(str(abs(i))) == 3]) >= 1:
        d = sum(nums) / len(nums)
        if 0 < d < maxi:
            ans.append(sum(nums))
print(len(ans), max(ans))
