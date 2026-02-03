from fnmatch import fnmatch as fnm


for val in range(750122 - 750122 % 8387, 10 ** 9 + 1, 8387):
    if fnm(str(val), '*75?122*'):
        print(val, val // 8387)
