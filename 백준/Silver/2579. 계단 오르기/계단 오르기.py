import sys

N = int(input())
stair = [[0, 0] for _ in range(N)]
score = int(input())
stair[0][0] = score
if N >= 2:
    score = int(input())
    stair[1][0] = stair[0][0] + score
    stair[1][1] = score
for i in range(2, N):
    score = int(sys.stdin.readline())
    stair[i][0] = stair[i - 1][1] + score
    stair[i][1] = max(stair[i - 2]) + score
print(max(stair[-1]))