import sys

N = int(input())
stack_time = []
stack_score = []
result = 0
for _ in range(N):
    assignment = list(map(int, sys.stdin.readline().split()))
    if assignment[0] == 0:
        if stack_time:
            stack_time[-1] -= 1
            if stack_time[-1] == 0:
                stack_time.pop()
                result += stack_score.pop()
        continue
    A, T = assignment[1], assignment[2]
    if T == 1:
        result += A
    else:
        stack_time.append(T - 1)
        stack_score.append(A)
print(result)