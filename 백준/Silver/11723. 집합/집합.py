import sys

N = int(input())
S = set()
for _ in range(N):
    line = sys.stdin.readline().split()
    if len(line) == 1:
        if line[0] == 'empty':
            S.clear()
        elif line[0] == 'all':
            S = set(range(1, 21))
    else:
        command = line[0]
        x = int(line[1])
        if command == 'add':
            S.add(x)
        elif command == 'remove':
            S.discard(x)
        elif command == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if x in S:
                S.remove(x)
            else:
                S.add(x)