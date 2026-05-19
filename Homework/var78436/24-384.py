# 9004

with open(r'../var78436/files/24-384.txt') as file:
    data = file.readline()

data = data.split('Z')
ans = 10 ** 10
for i in range(1, len(data) - 268 - 1):
    line = 'Z'.join(data[i:i + 269])
    ans = min(len(line) + 2, ans)
print(ans)
