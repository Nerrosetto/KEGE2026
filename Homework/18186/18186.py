with open(r'../18186/24_18186.txt') as file:
    data = file.readline()
data1 = data

for i in 'BCDFGH':
    data1 = data1.replace(i, '*')
for i in 'AE':
    data1 = data1.replace(i, '!')
data1 = data1.replace('**!', '_')
pos1 = 0
pos2 = 0
ans = []
for pos, i in enumerate(data1):
    if i == '_':
        if pos1 <= pos2:
            pos1 = pos
        else:
            pos2 = pos
    ans.append(len(data1[pos1:pos2 + 1]))

print(max(ans))
