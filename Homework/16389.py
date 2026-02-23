from fnmatch import fnmatch as fnm

for i in range(5023030 - 5023030 % 98591, 10 ** 10, 98591):
    if fnm(str(i), '5?2*3?3?'):
        print(i, i // 98591)
