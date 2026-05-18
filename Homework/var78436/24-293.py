with open(r'../var78436/files/24-293.txt') as file:
    data = file.readline()

data = data.split('D')
ans = 0
for i in range(len(data) - 100):
    line = 'D'.join(data[i:i + 101])
    for i in '1234567890':
        if i not in line:
            for t in ['DS', 'SD']:
                if t not in line:
                    ans = max(len(line), ans)
print(ans)
