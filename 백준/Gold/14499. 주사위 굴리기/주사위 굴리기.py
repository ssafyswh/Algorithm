def rotate(n):
    global now_x
    global now_y
    global bottom
    global dice1
    global dice2
    if n == 1:
        if now_x + 1 <= M - 1:
            now_x += 1
            dice1 = [dice1[3]] + dice1[:3]
            dice2[1] = dice1[2]
            dice2[3] = dice1[0]
        else:
            return 0
    elif n == 2:
        if now_x - 1 >= 0:
            now_x -= 1
            dice1 = dice1[1:] + [dice1[0]]
            dice2[1] = dice1[2]
            dice2[3] = dice1[0]
        else:
            return 0
    elif n == 3:
        if now_y - 1 >= 0:
            now_y -= 1
            dice2 = dice2[1:] + [dice2[0]]
            dice1[0] = dice2[3]
            dice1[2] = dice2[1]
        else:
            return 0
    else:
        if now_y + 1 <= N - 1:
            now_y += 1
            dice2 = [dice2[3]] + dice2[:3]
            dice1[0] = dice2[3]
            dice1[2] = dice2[1]
        else:
            return 0
    bottom = dice2[3]
    return 1


N, M, y, x, K = map(int, input().split())
cheese = []
dice1 = [0, 0, 0, 0]
dice2 = [0,
         0,
         0,
         0]
for _ in range(N):
    cheese.append(list(map(int, input().split())))
commands = list(map(int, input().split()))
now_y = y
now_x = x
bottom = dice1[0]
for i in range(K):
    command = commands[i]
    if rotate(command) == 1:
        if cheese[now_y][now_x] == 0:
            cheese[now_y][now_x] = bottom
        else:
            bottom = cheese[now_y][now_x]
            cheese[now_y][now_x] = 0
            dice1[0] = bottom
            dice2[3] = bottom
        print(dice1[2])