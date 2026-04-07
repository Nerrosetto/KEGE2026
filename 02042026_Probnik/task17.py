with open(r'./Files/17.txt') as file:
    data = [int(i) for i in file]

a = max(i for i in data if len(str(i)) == 2)
ans = []
for nums in zip(data, data[1:]):
    u1 = sum(len(str(i)) == 2 for i in nums) == 1
    if u1:
        u2 = sum(nums) % a == 0
        if u2:
            ans.append(sum(nums))
print(len(ans), max(ans))
