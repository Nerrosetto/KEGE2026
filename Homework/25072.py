ans = []
for i in range(1, 30000):
    a = ''
    p = f'{i:b}'
    for t in p:
        if t == '0':
            a += '1'
        else:
            a += '0'
    a = int(a, 2)
    if a < 30000:
        ans.append(a)
print(max(ans))
