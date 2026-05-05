with open(r'../Files/24_2942.txt') as file:
    data = file.readline()

cnt_max = cnt = i = 0
while i < len(data) - 1:
    if data[i] + data[i + 1] in 'AB AC':
        cnt += 1
        i += 2
    else:
        i += 1
        cnt_max = max(cnt, cnt_max)
        cnt = 0
cnt_max = max(cnt, cnt_max)

print(cnt_max)
