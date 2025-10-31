import sys

def merge_line(line, reverse=False):
    if reverse:
        line = line[::-1]

    stack = [x for x in line if x != 0]
    result_line = [0] * N
    idx = N - 1

    while stack:
        num = stack.pop()
        if result_line[idx] == 0:
            result_line[idx] = num
        elif result_line[idx] == num:
            result_line[idx] *= 2
            idx -= 1
        else:
            idx -= 1
            result_line[idx] = num

    if reverse:
        result_line.reverse()

    return result_line

def slide(direct, board_input):
    state = [row[:] for row in board_input]

    for i in range(N):
        if direct == 0:
            line = state[i]
            merged = merge_line(line)
            state[i] = merged

        elif direct == 1:
            line = [state[y][i] for y in range(N)]
            merged = merge_line(line)
            for y in range(N):
                state[y][i] = merged[y]

        elif direct == 2:
            line = state[i]
            merged = merge_line(line, reverse=True)
            state[i] = merged

        else:
            line = [state[y][i] for y in range(N)]
            merged = merge_line(line, reverse=True)
            for y in range(N):
                state[y][i] = merged[y]

    return state

def shuffle(now_board, n=0):
    global result
    if n == 5:
        return
    potential_max = max(map(max, now_board)) * (2 ** (5 - n))
    if potential_max <= result:
        return
    
    for i in range(4):
        next_state = slide(i, now_board)
        memo = (tuple(map(tuple, next_state)), n)
        if next_state == now_board or memo in memoization:
            continue
        result = max(result, max(map(max, next_state)))
        memoization.add(memo)
        shuffle(next_state, n + 1)

N = int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
memoization = set()
result = max(map(max, board))
shuffle(board)
print(result)