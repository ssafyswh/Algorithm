def sierpinski(y, x, n):
    if n == 3:
        board[y][x] = '*'
        board[y + 1][x - 1], board[y + 1][x + 1] = '*', '*'
        for n in range(-2, 3):
            board[y + 2][x + n] = '*'
        return
    half = n // 2
    sierpinski(y, x, half)
    sierpinski(y + half, x - half, half)
    sierpinski(y + half, x + half, half)


N = int(input())
board = [[' '] * (2 * N - 1) for _ in range(N)]
sierpinski(0, N - 1, N)
for row in board:
    print(''.join(row))