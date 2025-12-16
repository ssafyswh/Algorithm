import sys
input = sys.stdin.readline

R, C = map(int,input().split())

pipes = [input().strip() for _ in range(R)]
visited = [[False] * C for _ in range(R)]

def dig(nr, nc=0):
    global result
    if nc == C - 1:
        result += 1
        return True
    if nr > 0 and pipes[nr - 1][nc + 1] == '.' and not visited[nr - 1][nc + 1]:
        visited[nr - 1][nc + 1] = True
        if dig(nr - 1, nc + 1):
            return True
    if pipes[nr][nc + 1] == '.' and not visited[nr][nc + 1]:
        visited[nr][nc + 1] = True
        if dig(nr, nc + 1):
            return True
    if nr < R - 1 and pipes[nr + 1][nc + 1] == '.' and not visited[nr + 1][nc + 1]:
        visited[nr + 1][nc + 1] = True
        if dig(nr + 1, nc + 1):
            return True

    return False

result = 0
for r in range(R):
    visited[r][0] = True
    dig(r)

print(result)