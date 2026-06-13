from fnmatch import fnmatch as fnm

for i in range(37, 10 ** 8 + 1, 37):
    if fnm(str(i), '2*1234?6'):
        print(i, i // 37)
