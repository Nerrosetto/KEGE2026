ans = []
for N in range(1, 100000):
    R = f'{N:b}'
    if N % 3 == 0:
        R += R[-3:]
    else:
        R += f'{N % 3 * 3:b}'
    R = int(R, 2)
    ans.append([abs(130 - R), N])

for i in sorted(ans)[:10]:
    print(*i)
