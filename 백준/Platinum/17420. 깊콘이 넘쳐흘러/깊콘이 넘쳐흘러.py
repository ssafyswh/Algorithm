import sys
input = sys.stdin.readline

N = int(input())
A = [*map(int, input().split())]
B = [*map(int, input().split())]

gifts = [list(item) for item in zip(A, B)]
gifts.sort(key=lambda x: (x[1], x[0]))

result = 0
prev_max = gifts[0][1]
curr_max = -1

for i in range(N):
    if prev_max > gifts[i][0]:
        cnt = (prev_max - gifts[i][0] + 29) // 30
        gifts[i][0] += cnt * 30
        result += cnt
    curr_max = max(curr_max, gifts[i][0])

    if i + 1 < N and gifts[i][1] != gifts[i + 1][1]:
        prev_max = max(curr_max, gifts[i + 1][1])

print(result)