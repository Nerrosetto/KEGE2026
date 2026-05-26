from re import finditer
from string import printable as pri

with open(r'24_26551.txt') as file:
    data = file.readline()

data1 = data
for i in set(data1):
    if i not in pri[:14]:
        data1 = data1.replace(i, ' ')
data1 = data1.split()
ans = 0
for line in data1:
    line = line.rstrip('13579BD')
    line = line.lstrip('0')
    ans = max(ans, len(line))
print(ans)

# re:
pattern = r'[1-9ABCD][0-9ABCD]*[02468AC]'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
