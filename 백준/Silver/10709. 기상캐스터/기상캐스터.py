H, W = map(int, input().split())
sky = [list(input()) for _ in range(H)]
for h in range(H):
    count = 0
    cloud = False
    for w in range(W):
        if sky[h][w] == 'c':
            sky[h][w] = 0
            cloud = True
            count = 0
        elif sky[h][w] == '.':
            if cloud:
                count += 1
                sky[h][w] = count
            else:
                sky[h][w] = -1
for row in sky:
    print(' '.join(list(map(str, row))))