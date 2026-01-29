ans = []
for N in range(1, 30):
    R = bin(N)[2:]
    if sum(map(int, R)) % 2 == 0:
        R = '10' + R[:-2] + '00'
    else:
        R = '11' + R[:-2] + '11'
    ans.append(int(R, 2))
print(max(ans))
