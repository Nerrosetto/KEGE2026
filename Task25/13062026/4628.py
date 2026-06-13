from fnmatch import fnmatch as fnm

for i in range(161, 10 ** 8 + 1, 161):
    if fnm(str(i), '12*4?65'):
        print(i, i // 161)
