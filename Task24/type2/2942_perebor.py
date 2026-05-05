with open(r'../Files/24_2942.txt') as file:
    data = file.readline()

cnt_max = 0
for i in range(len(data) - 1):
    if data[i] + data[i + 1] in 'AB AC':
        cnt = 1
        for g in range(i + 2, len(data) - 1, 2):
            if data[g] + data[g + 1] in 'AB AC':
                cnt += 1
            else:
                break
        cnt_max = max(cnt, cnt_max)
print(cnt_max)
