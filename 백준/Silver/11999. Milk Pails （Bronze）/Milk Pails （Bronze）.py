def milk(n=0):
    if n + X <= M and not able[n + X]:
        able[n + X] = 1
        milk(n + X)
    if n + Y <= M and not able[n + Y]:
        able[n + Y] = 1
        milk(n + Y)
    return

X, Y, M = map(int, input().split())
able = [0] * (M + 1)
milk()
for i in range(M, -1, -1):
    if able[i]:
        print(i)
        break