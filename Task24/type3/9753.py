with open(r'../Files/24_9753.txt') as file:
    data = file.readline()

data = data.split('Y')
ans = 0
for i in range(len(data) - 150):
    line = 'Y'.join(data[i:i + 151])
    ans = max(len(line), ans)
print(ans)
