from fnmatch import fnmatch as fnm

for N in range(1004513 - 1004513 % 451, 10**9, 451):
    if fnm(str(N), '10?451*3'):
        print(N, N // 451)
