from fnmatch import fnmatch as fnm

for N in range(5401037 - 5401037 % 18579, 10**10, 18579):
    if fnm(str(N), '54?1?3*7'):
        print(N, N // 18579)
