from collections import deque


def rotate(gear, clock):
    if clock == 1:
        new = gear[7] + gear[:7]
    else:
        new = gear[1:] + gear[0]
    return new


gears = [input() for _ in range(4)]
K = int(input())

commands = [list(map(int, input().split())) for _ in range(K)]
for command in commands:
    final = [0] * 4
    check = [0] * 4
    g, c = command[0] - 1, command[1]
    final[g] = c
    q = deque([g])
    while q:
        g = q.popleft()
        if g - 1 >= 0 and check[g - 1] == 0:
            if gears[g][6] != gears[g - 1][2]:
                final[g - 1] = final[g] * (-1)
                q.append(g - 1)
            check[g - 1] = 1
        if g + 1 < 4 and final[g + 1] == 0:
            if gears[g][2] != gears[g + 1][6]:
                final[g + 1] = final[g] * (-1)
                q.append(g + 1)
            check[g + 1] = 1
    for i in range(4):
        if final[i] != 0:
            gears[i] = rotate(gears[i], final[i])
result = 0
count = 1
for gear in gears:
    if gear[0] == '1':
        result += count
    count *= 2
print(result)