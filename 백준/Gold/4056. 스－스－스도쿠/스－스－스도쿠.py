def sudoku(n=0):
    if n == num_blank:
        for r in question:
            print(''.join(list(map(str, r))))
        return True
    
    by, bx = blank[n]
    for i in range(1, 10):
        if i in row[by]:
            continue
        if i in column[bx]:
            continue
        if i in block[bx // 3 + (by // 3) * 3]:
            continue
        question[by][bx] = i
        row[by].add(i)
        column[bx].add(i)
        block[bx // 3 + (by // 3) * 3].add(i)
        if sudoku(n + 1):
            return True
        question[by][bx] = 0
        row[by].remove(i)
        column[bx].remove(i)
        block[bx // 3 + (by // 3) * 3].remove(i)
        
    return False

def is_valid():
    for y in range(9):
        for x in range(9):
            if question[y][x] == 0:
                blank.append((y, x))
                continue
            num = question[y][x]
            if num in row[y]:
                return False
            row[y].add(num)
            if num in column[x]:
                return False
            column[x].add(num)
            if num in block[x // 3 + (y // 3) * 3]:
                return False
            block[x // 3 + (y // 3) * 3].add(num)
    return True
    
T = int(input())
for t in range(T):
    if t > 0:
        print()
    question = [list(map(int, list(input().strip()))) for _ in range(9)]
    row = [set() for _ in range(9)]
    column = [set() for _ in range(9)]
    block = [set() for _ in range(9)]
    blank = []
    if not is_valid():
        print('Could not complete this grid.')
        continue
    num_blank = len(blank)
    if not sudoku():
        print('Could not complete this grid.')