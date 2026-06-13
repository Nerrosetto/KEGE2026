from fnmatch import fnmatch as fnm

for i in range(141, 10 ** 8 + 1, 141):
    if fnm(str(i), '1234*7'):
        print(i, i // 141)
