from re import finditer

with open(r'../Files/24_4627.txt') as file:
    data = file.readline()

# re:
pattern = r'(NPO|PNO)+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 3)

# zamena:
data1 = data.replace('NPO', '*').replace('PNO', '*')

for i in set(data):
    if i != '*':
        data1 = data1.replace(i, ' ')
data1 = data1.split()
print(len(max(data1, key=len)))

# ukazat:
cnt_max = cnt = i = 0
while i < len(data) - 2:
    if data[i] + data[i + 1] + data[i + 2] in 'NPO PNO':
        cnt += 1
        i += 3
    else:
        i += 1
        cnt_max = max(cnt, cnt_max)
        cnt = 0
cnt_max = max(cnt_max, cnt)
print(cnt_max)

# perebor:
cnt_max = 0
for i in range(len(data) - 2):
    if data[i] + data[i + 1] + data[i + 2] in 'PNO NPO':
        cnt = 1
        for g in range(i + 3, len(data) - 1, 3):
            if data[g] + data[g + 1] + data[g + 2] in 'PNO NPO':
                cnt += 1
            else:
                break
        cnt_max = max(cnt, cnt_max)
print(cnt_max)
