from itertools import product as pro

with open(r'../7624/24_7624.txt') as file:
    data = file.readline()

check = [''.join(i) for i in pro('XYZ', repeat=2)]
data1 = data

for i in check:
    data1 = data1.replace(i, '*')

data1 = data1.replace('*', '* *')
data1 = data1.split()

print(len(max(data1, key=len)))
