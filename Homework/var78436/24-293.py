# 7438

with open(r'../var78436/files/24-293.txt') as file:
    data = file.readline()

data = data.replace('SD', 'DS').replace('DS', 'D S').split()
ans = 0
for i in range(len(data) - 100):
    line = 'DS'.join(data[i:i + 101])
    for i in '1234567890':
        if i not in line:
            if 'DS' not in line:
                ans = max(len(line), ans)
print(ans)
