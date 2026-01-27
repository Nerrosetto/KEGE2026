from fnmatch import fnmatch as fnm

for N in range(1021394 - 1021394 % 2023, 10 ** 10, 2023):
    if fnm(str(N), '1?2139*4'):
        print(N, N // 2023)
