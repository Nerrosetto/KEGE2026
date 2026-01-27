from fnmatch import fnmatch as fnm

for N in range(2123406 - 2123406 % 37, 10**8, 37):
    if fnm(str(N), '2*1234?6'):
        print(N, N // 37)
