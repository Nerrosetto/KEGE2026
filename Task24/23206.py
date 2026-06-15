with open(r'../Task24/Files/24_23206.txt') as file:
    data = file.readline()

data = data.lower()

for i in range(0, 10, 2):
    a = str(i)
    b = ' ' + a
    data = data.replace(a, b)

data = data.split()

maxi = 0
for i in data:
    if i.count('s') == 35:
        maxi = max(maxi, len(i))
    elif i.count('s') > 35:
        for t in range(len(i)):
            if i[:-t].count('s') == 35:
                maxi = max(maxi, len(i[:-t]))
print(maxi)
