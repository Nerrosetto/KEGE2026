with open(r'../4682/24_4682.txt') as file:
    data = file.readline()
check = [f'E{i}' for i in 'BCD']
check += [f'A{i}' for i in 'BCD']
data1 = data

for i in check:
    data1 = data1.replace(i, '*')

data1 = data1.replace('B', ' ').replace('C', ' ').replace('D', ' ').replace('A', ' ').replace('E', ' ')
data1 = data1.split()

print(len(max(data1, key=len)))
