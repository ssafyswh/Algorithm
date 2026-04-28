import sys
N = int(input())
for _ in range(N):
    line = sys.stdin.readline().strip()
    if line[:10] == 'Simon says':
        print(line[10:])
