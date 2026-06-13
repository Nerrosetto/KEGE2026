from string import printable as pri

with open(r'../kege_25198501/files/24_27777.txt') as file:
    data = file.readline().lower()

for i in pri[12:pri.index('z') + 1]:
    data = data.replace(i, '*')

data = data.split('*')
print(len(max(data, key=len)))
