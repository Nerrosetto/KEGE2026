from string import printable as pri
from re import finditer

with open(r'../Files/24_3228.txt') as file:
    data = file.readline()

pattern = r'(AB|AC)+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 2)

data = data.replace('AB', '*')
data = data.replace('AC', '*')
for i in pri[pri.index('A'):pri.index('Z') + 1]:
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))
