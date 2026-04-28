r, c = map(int, input().split())
board = [input() for _ in range(10)]
row = [1] * 10
col = [1] * 10
for y in range(10):
    for x in range(10):
        if board[y][x] == 'o':
            row[y] = 0
            col[x] = 0
count = 0
result1 = 0
while True:
    if r - 1 + count < 10 and row[r - 1 + count]:
        result1 = count
        break
    elif r - 1 - count >= 0 and row[r - 1 - count]:
        result1 = count
        break
    count += 1
count = 0
result2 = 0
while True:
    if c - 1 + count < 10 and col[c - 1 + count]:
        result2 = count
        break
    elif c - 1 - count >= 0 and col[c - 1 - count]:
        result2 = count
        break
    count += 1
print(result1 + result2)