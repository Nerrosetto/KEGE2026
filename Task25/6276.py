from fnmatch import fnmatch as fnm

for N in range(2023, 10 ** 10 + 1, 2023):
    st = str(N)
    if fnm(st, '1?1?1?1*1'):
        if sum(map(int, st)) == 22:
            print(N)
