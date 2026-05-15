from re import finditer

with open(r'../12254/24_12254.txt') as file:
    data = file.readline()

# zamena
data1 = data

data1 = data1.replace('RSQ', '***')
data1 = data1.replace('SQ*', ' ***').replace('Q*', ' **')
data1 = data1.replace('*RS', '!!! ').replace('*R', '!! ').replace('*S', '!! ')
data1 = data1.replace('*QR', '!!! ')

for i in 'RSQ':
    data1 = data1.replace(i, ' ')

data1 = data1.split()
print(len(max(data1, key=len)))

# re
pattern = r''