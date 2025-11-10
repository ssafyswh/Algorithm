import sys

board = [list(sys.stdin.readline().strip()) for _ in range(9)]
rows = [set() for _ in range(9)]
columns = [set() for _ in range(9)]
blocks = [set() for _ in range(9)]
blank = []
num_of_blank = len(blank)

for y in range(9):
    for x in range(9):
        if board[y][x] != '0':
            num = board[y][x]
            rows[y].add(num)
            columns[x].add(num)
            blocks[x // 3 + (y // 3) * 3].add(num)
        else:
            blank.append((y, x))
num_of_blank = len(blank)
nums = list(map(str, range(1, 10)))

def sudoku(n=0):
    if n == num_of_blank:
        for row in board:
            print(''.join(row))
        return True

    by, bx = blank[n]
    for num in nums:
        if num in rows[by]:
            continue
        if num in columns[bx]:
            continue
        if num in blocks[bx // 3 + (by // 3) * 3]:
            continue
        board[by][bx] = num
        rows[by].add(num)
        columns[bx].add(num)
        blocks[bx // 3 + (by // 3) * 3].add(num)
        if sudoku(n + 1):
            return True
        board[by][bx] = '0'
        rows[by].remove(num)
        columns[bx].remove(num)
        blocks[bx // 3 + (by // 3) * 3].remove(num)
    else:
        return False

sudoku()