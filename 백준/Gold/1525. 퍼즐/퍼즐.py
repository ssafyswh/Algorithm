from collections import deque

board = []
for _ in range(3):
    board.extend(list(map(int, input().split())))
answer = (1, 2, 3, 4, 5, 6, 7, 8, 0)
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))


def find_start():
    n = board.index(0)
    y, x = n // 3, n % 3
    return y, x

def solve():
    sy, sx = find_start()
    if tuple(board) == answer:
        return 0
    memoization = set(tuple(board))
    q = deque([(tuple(board), sy, sx, 0)])
    while q:
        now_state, ny, nx, cnt = q.popleft()
        now_state = list(now_state)
        nxt_cnt = cnt + 1
        for d in delta:
            dy, dx = ny + d[0], nx + d[1]
            if not (0 <= dy < 3 and 0 <= dx < 3):
                continue
            now_state[ny * 3 + nx], now_state[dy * 3 + dx] = now_state[dy * 3 + dx], 0
            memo = tuple(now_state)
            if memo == answer:
                return nxt_cnt
            if memo not in memoization:
                memoization.add(memo)
                q.append((memo, dy, dx, nxt_cnt))
            now_state[ny * 3 + nx], now_state[dy * 3 + dx] = 0, now_state[ny * 3 + nx]
    return -1
    
print(solve())