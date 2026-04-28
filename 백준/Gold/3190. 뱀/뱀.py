from collections import deque


def snake_turn(now, command):
    if command == 'L':
        if now < 3:
            return now + 1
        else:
            return 0
    elif command == 'D':
        if now > 0:
            return now - 1
        else:
            return 3


N = int(input())
board = [['N'] * N for _ in range(N)]
board[0][0] = 'S'
K = int(input())
delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
for _ in range(K):
    apple = list(map(int, input().split()))
    apple_y = apple[0] - 1
    apple_x = apple[1] - 1
    board[apple_y][apple_x] = 'A'
L = int(input())
time = 0
snake = deque([(0, 0)])
head = 3
flag = False
for _ in range(L):
    move = input().split()
    goal, turn = int(move[0]), move[1]
    while time < goal:
        time += 1
        y, x = snake.pop()
        dy = y + delta[head][0]
        dx = x + delta[head][1]
        if 0 <= dy < N and 0 <= dx < N and board[dy][dx] != 'S':
            snake.append((y, x))
            snake.append((dy, dx))
            if board[dy][dx] != 'A':
                tail_y, tail_x = snake.popleft()
                board[tail_y][tail_x] = 'N'
            board[dy][dx] = 'S'
        else:
            flag = True
            break
    if flag:
        break
    head = snake_turn(head, turn)
else:
    while True:
        time += 1
        y, x = snake.pop()
        dy = y + delta[head][0]
        dx = x + delta[head][1]
        if 0 <= dy < N and 0 <= dx < N and board[dy][dx] != 'S':
            snake.append((y, x))
            snake.append((dy, dx))
            if board[dy][dx] != 'A':
                tail_y, tail_x = snake.popleft()
                board[tail_y][tail_x] = 'N'
            board[dy][dx] = 'S'
        else:
            flag = True
            break
print(time)