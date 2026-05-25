from string import printable as pri

with open(r'24_26551.txt') as file:
    data = file.readline()

for i in set(data):
    if i in pri[:14]:
        data = data.replace(i, '*')
    else:
        data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))
