import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

row = [set() for _ in range(9)]
column = [set() for _ in range(9)]
block = [set() for _ in range(9)]
blank = []

for y in range(9):
    for x in range(9):
        num = board[y][x]
        if num:
            row[y].add(num)
            column[x].add(num)
            block[(y // 3) * 3 + x // 3].add(num)
        else:
            blank.append((y, x))

remain = len(blank)

def sudoku(n=0):
    if n == remain:
        for line in board:
            print(*line)
        return True

    blank_y, blank_x = blank[n]
    for i in range(1, 10):
        if i in row[blank_y]:
            continue
        if i in column[blank_x]:
            continue
        if i in block[(blank_y // 3) * 3 + blank_x // 3]:
            continue
        board[blank_y][blank_x] = i
        row[blank_y].add(i)
        column[blank_x].add(i)
        block[(blank_y // 3) * 3 + blank_x // 3].add(i)
        if sudoku(n + 1):
            return True
        board[blank_y][blank_x] = 0
        row[blank_y].remove(i)
        column[blank_x].remove(i)
        block[(blank_y // 3) * 3 + blank_x // 3].remove(i)
    return False

sudoku()