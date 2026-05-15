with open(r'../Files/24_9854.txt') as file:
    data = file.readline()

for i in 'ABC':
    data = data.replace(i, '*')
for i in '89':
    data = data.replace(i, '!')

data = data.replace('*!', '* !').replace('!*', '! *').split()
print(len(max(data, key=len)))
