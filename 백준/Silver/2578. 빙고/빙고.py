def find(n):
    for y in range(5):
        for x in range(5):
            if board[y][x] == n:
                return y, x


board = [list(map(int, input().split())) for _ in range(5)]
order = [list(map(int, input().split())) for _ in range(5)]
row = [0] * 5
column = [0] * 5
diagonal = [0] * 2
bingo_count = 0
result = - 1
while bingo_count < 3:
    result += 1
    now = order[result // 5][result % 5]
    ny, nx = find(now)
    row[ny] += 1
    if row[ny] == 5:
        bingo_count += 1
    column[nx] += 1
    if column[nx] == 5:
        bingo_count += 1
    if ny == nx:
        diagonal[0] += 1
        if diagonal[0] == 5:
            bingo_count += 1
    if ny + nx == 4:
        diagonal[1] += 1
        if diagonal[1] == 5:
            bingo_count += 1
print(result + 1)