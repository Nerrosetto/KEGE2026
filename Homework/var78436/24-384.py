with open(r'../var78436/files/24-384.txt') as file:
    data = file.readline()

data = data.split('Z')
ans = 0
for i in range(len(data) - 270):
    line = 'Z'.join(data[i:i + 271])
    if len(line) == 0 or ans == 0:
        ans = len(line)
    else:
        ans = min(len(line), ans)
print(ans)
