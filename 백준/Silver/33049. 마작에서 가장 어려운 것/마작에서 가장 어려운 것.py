p3, p4, p0 = map(int, input().split())

def mahjong():
    global p3, p4, p0

    game = 0
    not_game = 0

    game += p4 // 4
    p4 = p4 % 4
    if p4:
        p0 -= 4 - p4
        game += 1
        if p0 < 0:
            print(-1)
            return

    not_game += p3 // 3
    p3 = p3 % 3
    if p3:
        p0 -= 3 - p3
        not_game += 1
        if p0 < 0:
            print(-1)
            return

    for i in range(p0 // 4, -1, -1):
        if (p0 - 4 * i) % 3 == 0:
            game += i
            not_game += (p0 - 4 * i) // 3
            print(not_game, game)
            return

    print(-1)
    return

mahjong()