from re import finditer

with open(r'../15339/24_15339.txt') as file:
    data = file.readline()

# zamena
data1 = data
for i in 'ABC':
    data1 = data1.replace(i, '*')
for i in '6789':
    data1 = data1.replace(i, '_')

while '*_' in data1 or '_*' in data1:
    data1 = data1.replace('*_', '* _').replace('_*', '_ *').split()
print(len(max(data1, key=len)))

# re
pattern = r'[6789]?([ABC][6789]*|[6789][ABC]*)[ABC]?'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
