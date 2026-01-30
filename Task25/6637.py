from fnmatch import fnmatch as fnm

for N in range(1021394 - 1021394 % 3052, 10 ** 10, 3052):
    if fnm(str(N), '1?2139*4'):
        print(N, N // 3052)
