from re import finditer

with open(r'../17878/24_17878.txt') as file:
    data = file.readline()

data1 = data
num = r'([1-9][0-9]*|0)'
pattern = rf'({num}[-*])+{num}'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
