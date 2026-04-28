N = int(input())
snare = [[0] * N for _ in range(N)]
x = N // 2
y = N // 2
snare[x][y] = 1
x_move = 1
x_move_count = 0
x_move_direct = -1
y_move = 1
y_move_count = 0
y_move_direct = 1
turn = 1
for num in range(2, N ** 2 + 1):
    if turn == 1:
        x += x_move_direct
        x_move_count += 1
        if x_move == x_move_count:
            x_move += 1
            x_move_count = 0
            x_move_direct *= -1
            turn *= -1
    else:
        y += y_move_direct
        y_move_count += 1
        if y_move == y_move_count:
            y_move += 1
            y_move_count = 0
            y_move_direct *= -1
            turn *= -1
    snare[x][y] = num
for row in snare:
    print(' '.join(list(map(str, row))))

target = int(input())
for xt in range(N):
    for yt in range(N):
        if snare[xt][yt] == target:
            print(xt + 1, yt + 1)
            break