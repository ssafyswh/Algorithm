def bishop_black(n=0, filled=0):
    if n == N:
        result[0] = max(result[0], filled)
        return
    for i in range(len_row_black):
        if not blank_black[n][i]:
            continue
        if visited_black[i]:
            continue
        visited_black[i] = True
        bishop_black(n + 1, filled + 1)
        visited_black[i] = False
    else:
        bishop_black(n + 1, filled)

def bishop_white(n=0, filled=0):
    if n == N - 1:
        result[1] = max(result[1], filled)
        return
    for i in range(len_row_white):
        if not blank_white[n][i]:
            continue
        if visited_white[i]:
            continue
        visited_white[i] = True
        bishop_white(n + 1, filled + 1)
        visited_white[i] = False
    else:
        bishop_white(n + 1, filled)
        
N = int(input())
chess = [input().split() for _ in range(N)]
if N > 1:
    num_of_diagonal_line = 2 * N - 1
    blank_black = [[False] * (N if N % 2 else N - 1) for _ in range(N)]
    len_row_black = len(blank_black[0])
    blank_white = [[False] * (N - 1 if N % 2 else N) for _ in range(N - 1)]
    len_row_white = len(blank_white[0])
    for n in range(0, num_of_diagonal_line, 2):
        for k in range(n + 1):
            y, x = k, n - k
            if not (0 <= y < N and 0 <= x < N):
                continue
            if chess[y][x] == '1':
                blank_black[n // 2][(len_row_black // 2 - n // 2) + k] = True
    
    for n in range(1, num_of_diagonal_line, 2):
        for k in range(n + 1):
            y, x = k, n - k
            if not (0 <= y < N and 0 <= x < N):
                continue
            if chess[y][x] == '1':
                blank_white[n // 2][(len_row_white // 2 - n // 2 - 1) + k] = True
    
    result = [0, 0]
    visited_black = [False] * len_row_black
    visited_white = [False] * len_row_white
    bishop_black()
    bishop_white()
    print(sum(result))

else:
    print(int(chess[0][0]))