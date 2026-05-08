from itertools import product as pro

with open(r'../7600/24_7600.txt') as file:
    data = file.readline()
check = [''.join(i) for i in pro('QRS', repeat=2)]
data1 = data

for i in check:
    data1 = data1.replace(i, '*')

data1 = data1.replace('*', '* *')
data1 = data1.split()

print(len(max(data1, key=len)))
