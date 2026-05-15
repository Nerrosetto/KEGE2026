with open(r'../Files/24_10105.txt') as file:
    data = file.readline()

# zamena
data = data.split('T')
ans = 0
for i in range(len(data) - 100):
    line = 'T'.join(data[i:i + 101])
    ans = max(len(line), ans)
print(ans)
