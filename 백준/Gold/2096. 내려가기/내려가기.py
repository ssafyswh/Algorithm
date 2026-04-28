import sys

N = int(input())
max_board = []
min_board = []
for i in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    if not i:
        max_board = [a, b, c]
        min_board = [a, b, c]
        continue
    temp_max_board = [0] * 3
    temp_min_board = [0] * 3
    temp_max_board[0] = a + max(max_board[0: 2])
    temp_max_board[1] = b + max(max_board)
    temp_max_board[2] = c + max(max_board[1:])
    temp_min_board[0] = a + min(min_board[0: 2])
    temp_min_board[1] = b + min(min_board)
    temp_min_board[2] = c + min(min_board[1:])
    max_board = temp_max_board
    min_board = temp_min_board
print(max(max_board), min(min_board))