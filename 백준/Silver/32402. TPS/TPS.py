N = int(input())
player = [0, 0]
direct = 0
rotate = ((0, 1), (1, 0), (0, -1), (-1, 0))
for _ in range(N):
    command = input()
    if command == 'W':
        player[0] += rotate[direct][0]
        player[1] += rotate[direct][1]
    elif command == 'A':
        player[0] += rotate[(direct + 3) % 4][0]
        player[1] += rotate[(direct + 3) % 4][1]
    elif command == 'S':
        player[0] += rotate[(direct + 2) % 4][0]
        player[1] += rotate[(direct + 2) % 4][1]
    elif command == 'D':
        player[0] += rotate[(direct + 1) % 4][0]
        player[1] += rotate[(direct + 1) % 4][1]
    elif command == 'MR':
        direct = (direct + 1) % 4
    elif command == 'ML':
        direct = (direct + 3) % 4
    print(*player, player[0] - rotate[direct][0], player[1] - rotate[direct][1])