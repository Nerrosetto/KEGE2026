with open(r'.\Files\17_9748.txt') as file:
    data = [int(x) for x in file]
ans = []
maxi = max(i for i in data if str(i)[-2:] == '15')
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = num1 + num2 + num3 >= maxi
    u2 = len(str(num1)) == 4 and (not any((len(str(num2)) == 4, len(str(num3)) == 4)))
    u3 = len(str(num2)) == 4 and (not any((len(str(num1)) == 4, len(str(num3)) == 4)))
    u4 = len(str(num3)) == 4 and (not any((len(str(num2)) == 4, len(str(num1)) == 4)))
    if u1 and any((u2, u3, u4)):
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))

#################################################
with open(r'.\Files\17_9748.txt') as file:
    data = [int(x) for x in file]
ans = []
maxi = max(i for i in data if str(i)[-2:] == '15')
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = len(str(num1)) == 4
    u2 = 1000 <= num2 <= 9999
    u3 = len(str(num3)) == 4
    if u1 + u2 + u3 == 1 and num1 + num2 + num3 >= maxi:
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))
