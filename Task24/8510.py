with open(r'C:\Users\Acer\PycharmProjects\KEGE20261\Task24\Files\24_8510.txt') as file:
    data = file.readline()

data = data.replace('O', 'P').replace('N', 'P')
while 'NN' in data:
    data = data.replace('NN', 'N N')

print(max(len(i) for i in data.split()))
