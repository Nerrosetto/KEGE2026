with open(r'24_23281.txt') as file:
    data = file.readline()

ans = []
data = data.split('Y')
for i in range(len(data) - 80):
    L = data[i:i + 81]
    L = 'Y'.join(L)
    if L.count('2025') >= 90 and L.count('Y') == 80:
        ans.append(len(L))
print(max(ans))
