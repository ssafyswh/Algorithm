N = int(input())
board = [['0'] * (N + 1) for _ in range(N + 1)]
score = {'0': 0}
for i in range(1, 10):
    score[str(i)] = i
    score[chr(ord('A') + i - 1)] = -i

for y in range(1, N + 1):
    line = list(input())
    for x in range(1, N + 1):
        board[y][x] = line[x - 1]

selected = [0] * (N + 1)
MAX = float('inf')
result = [MAX, -MAX]

def check_cycle():
    checked = [False] * (N + 1)
    cnt = 0
    for start in range(1, N + 1):
        if checked[start]:
            continue
        now = start
        while True:
            now = selected[now]
            if checked[now]:
                break
            checked[now] = True
        cnt += 1
    return cnt

def dominomidomado(n=0, now_score=1):
    if n == N:
        num_of_cycle = check_cycle()
        final_score = (-1) ** (num_of_cycle + 1) * now_score
        result[0] = min(result[0], final_score)
        result[1] = max(result[1], final_score)
        return
    for right in range(1, N + 1):
        if selected[right]:
            continue
        selected[right] = n + 1
        dominomidomado(n + 1, now_score * score[board[right][n + 1]])
        selected[right] = 0
    
dominomidomado()
print(result[0])
print(result[1])