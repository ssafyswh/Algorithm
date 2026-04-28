import sys

def dfs(y, x, remain):
    global result
    if y == 8:
        result += 1
        return
    if x == 7:
        dfs(y + 1, 0, remain)
        return
    if visited[y][x]:
        dfs(y, x + 1, remain)
        return

    for d in range(2):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < 8 and 0 <= nx < 7 and not visited[ny][nx]:
            a, b = board[y][x], board[ny][nx]
            domino = (min(a, b), max(a, b))
            if domino in remain:
                visited[y][x] = visited[ny][nx] = True
                remain.remove(domino)

                dfs(y, x + 1, remain)
                remain.add(domino)
                visited[y][x] = visited[ny][nx] = False
                
dominos = set()
for i in range(7):
    for j in range(i, 7):
        dominos.add((i, j))
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(8)]
visited = [[False] * 7 for _ in range(8)]
result = 0

dy = [0, 1]
dx = [1, 0]

dfs(0, 0, set(dominos))
print(result)