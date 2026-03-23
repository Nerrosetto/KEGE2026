with open(r'../files/24_1866.txt') as file:
    data = file.readline()

data = data.replace('NOP', 'NO OP NP')
data = data.split()
print(len(max(data, key=len)))
