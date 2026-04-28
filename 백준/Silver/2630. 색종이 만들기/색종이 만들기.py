def origami(N, pixels):
    global white0
    global blue1
    first = pixels[0][0]
    able = True
    for i in range(N):
        for j in range(N):
            if pixels[i][j] != first:
                able = False
                break
        if not able:
            break
    if able:
        if first == 1:
            blue1 += 1
            return
        else:
            white0 += 1
            return
    n = N // 2
    quad1 = [row[0:n] for row in pixels[0:n]]
    quad2 = [row[n:N] for row in pixels[0:n]]
    quad3 = [row[0:n] for row in pixels[n:N]]
    quad4 = [row[n:N] for row in pixels[n:N]]
    origami(n, quad1)
    origami(n, quad2)
    origami(n, quad3)
    origami(n, quad4)
    return

N = int(input())
pixels = [list(map(int, input().split())) for _ in range(N)]
white0 = 0
blue1 = 0
origami(N, pixels)
print(white0)
print(blue1)