from fnmatch import fnmatch as fnm

for i in range(10101011 - 10101011 % 2023, 10 ** 10, 2023):
    if fnm(str(i), '1?1?1?1*1') and sum(map(int, str(i))) == 22:
        print(i)