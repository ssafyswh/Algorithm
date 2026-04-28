import sys

def game(n=1, count=0):
    global result
    if n >= 100:
        result = min(result, count)
        return
    if board[n]:
        n = board[n]
    if visited[n] > count:
        visited[n] = count
    else:
        return
    for i in range(1, 7):
        game(n + i, count + 1)
        if n + i >= 100:
            break

N, M = map(int, input().split())
board = [0] * 101
visited = [101] * 101
for _ in range(N + M):
    x, y = map(int, sys.stdin.readline().split())
    board[x] = y
result = 101
game()
print(result)