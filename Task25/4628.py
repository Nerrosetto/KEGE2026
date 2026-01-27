from fnmatch import fnmatch as fnm
from string import printable as pri
from itertools import product as pro

for N in range(124065 - 124065 % 161, 10 ** 8 + 1, 161):
    if fnm(str(N), '12*4?65'):
        print(N, N // 161)
print('#' * 142)
ans = []
for V in pri[:10]:
    for L in range(0, 3):
        for S in pro(pri[:10], repeat=L):
            num = int(f'12{''.join(S)}4{V}65')
            if num % 161 == 0 and num <= 10 ** 8:
                ans.append([num, num // 161])
for i in sorted(ans):
    print(*i)
