with open(r'../1975/24_1975.txt') as file:
    data = file.readline()

data = data.replace('Q', 'N').replace('R', 'N').replace('S', 'N')
while 'PP' in data:
    data = data.replace('PP', 'P P')

print(max(len(i) for i in data.split()))
