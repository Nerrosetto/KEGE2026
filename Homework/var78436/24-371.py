with open(r'../var78436/files/24-371.txt') as file:
    data = file.readline()

data = data.split('M')
ans = 0
for i in range(len(data) - 112):
    line = 'M'.join(data[i:i + 113])
    ans = max(len(line), ans)
print(ans)
