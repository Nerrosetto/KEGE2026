with open(r'Files/17_27629.txt') as file:
    data = [int(i) for i in file]

ans = []
maxi = max(i for i in data if len(str(abs(i))) == 4 and abs(i) % 100 == 43)
for nums in zip(data, data[1:]):
    if sum(1 for i in nums if len(str(abs(i))) == 4) >= 1:
        if sum(nums) ** 2 < maxi ** 2:
            ans.append(sum(nums) ** 2)
print(len(ans), max(ans))
