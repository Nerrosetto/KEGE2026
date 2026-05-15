with open(r'../21717/24_21717.txt') as file:
    data = file.readline()

# zamena
data = data.replace('RSQ', 'Rsq rsQ')
data = data.split(' ')
# заменяем на маленькие буквы, так как их в файле нет.
ans = len(data) ** 2
for i in range(len(data) - 128 - 1):  # объяснение на видео 15052026
    line = ''.join(data[i:i + 129]).replace('sqrs', 'S')
    # из-за усложнения задачи, берём из следующей последовательности символ => - 1.
    for j in data[i + 129][3:]:
        line += j
        if j != 'Q':
            break
    ans = min(len(line), ans)
print(ans)
