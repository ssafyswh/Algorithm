board = [['W'] * 8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0:
                board[i][j] = 'B'
        else:
            if j % 2 == 1:
                board[i][j] = 'B'
N, M = list(map(int, input().split()))
input_board = []
for _ in range(N):
    input_board.append(list(input()))
min_differ = -1
for n in range(N - 7):
    for m in range(M - 7):
        temp_board = []
        for k in range(8):
            temp_board.append(input_board[n + k][m : m + 8])
        differ_count = 0
        for x in range(8):
            for y in range (8):
                if temp_board[x][y] != board[x][y]:
                    differ_count += 1
        if differ_count > 32:
            differ_count = 64 - differ_count
        if min_differ == -1:
            min_differ = differ_count
        else:
            if min_differ > differ_count:
                min_differ = differ_count
print(min_differ)