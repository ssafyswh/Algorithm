T = int(input())
for _ in range(T):
    balloons = input()
    amber = 0
    brass = 0
    for balloon in balloons:
        if balloon == 'a':
            amber += 1
        else:
            brass += 1
    print(min([amber, brass]))