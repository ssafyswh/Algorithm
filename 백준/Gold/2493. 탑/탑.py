import sys
N = int(input())
towers = list(map(int, sys.stdin.readline().split()))
stack = []
possible = []
result = []
for n in range(N):
    if stack:
        while stack and stack[-1] < towers[n]:
            stack.pop()
            possible.pop()
        if stack:
            result.append(possible[-1])
        else:
            result.append(0)
        stack.append(towers[n])
        possible.append(n + 1)        
    else:
        stack.append(towers[n])
        result.append(0)
        possible.append(n + 1)
print(' '.join(list(map(str, result))))