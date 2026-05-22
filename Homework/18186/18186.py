from re import finditer

with open(r'../18186/24_18186.txt') as file:
    data = file.readline()
data1 = data

# re:
SSG = R'[^AE]{2}[AE]'
pattern = rf'(?<={SSG}).*?(?={SSG})'  # ?<= - "обязательно в начале", ?= - "обязательно в конце"
# ? отключает "жадность" регулярки.
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) + 6)

# zamena:
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
    ans.append(len(data1[pos1:pos2 + 1]) + 6)
print(max(ans))
