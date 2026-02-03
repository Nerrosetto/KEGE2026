ans = []
for N in range(1, 99999):
    R = bin(N + 2)[2:]
    for i in range(2):
        R += bin(sum(map(int, R)) % 2)[2:]
    R = int(R, 2)
    if R < 61:
        ans.append(N)
print(max(ans))
