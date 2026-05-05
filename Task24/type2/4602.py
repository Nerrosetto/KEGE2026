with open(r'../Files/24_4602.txt') as file:
    data = file.readline()

# zamena:
check = ['BO', 'BA', 'CO', 'CA', 'DA', 'DO']
data1 = data

for i in check:
    data1 = data1.replace(i, '*')

for i in set(data1):
    if i != '*':
        data1 = data1.replace(i, ' ')

data1 = data1.split()

print(len(max(data1, key=len)))

# ukazat:
cnt_max = cnt = i = 0
while i < len(data) - 1:
    if data[i] + data[i + 1] in check:
        i += 2
        cnt += 1
    else:
        i += 1
        cnt_max = max(cnt, cnt_max)
        cnt = 0
cnt_max = max(cnt_max, cnt)
print(cnt_max)

# perebor:
cnt_max = 0
for i in range(len(data) - 1):
    if data[i] + data[i + 1] in check:
        cnt = 1
        for g in range(i + 2, len(data) - 1, 2):
            if data[g] + data[g + 1] in check:
                cnt += 1
            else:
                break
        cnt_max = max(cnt, cnt_max)
print(cnt_max)
