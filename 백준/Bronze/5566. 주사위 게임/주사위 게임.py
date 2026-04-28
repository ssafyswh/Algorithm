N, M = map(int, input().split())
board = [0] * (N + 1)
for i in range(1, N + 1):
    board[i] = int(input())
now = 1
result = 0
for j in range(M):
    result += 1
    now += int(input())
    if now >= N:
        break
    now += board[now]
    if now >= N:
        break
print(result)