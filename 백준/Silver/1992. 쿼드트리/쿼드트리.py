def QuadTree(N, pixels):
    first_pixel = pixels[0][0]
    able = True
    for row in pixels:
        for pixel in row:
            if pixel != first_pixel:
                able = False
                break
        if not able:
            break
    if able:
        return first_pixel
    n = N // 2
    result = []
    quad1 = [row[0:n] for row in pixels[0:n]]
    quad2 = [row[n:N] for row in pixels[0:n]]
    quad3 = [row[0:n] for row in pixels[n:N]]
    quad4 = [row[n:N] for row in pixels[n:N]]
    result.append(QuadTree(n, quad1))
    result.append(QuadTree(n, quad2))
    result.append(QuadTree(n, quad3))
    result.append(QuadTree(n, quad4))
    return tuple(result)

num = int(input())
pixels = [list(map(int, list(input()))) for _ in range(num)]
sample = list(str(QuadTree(num, pixels)))
for char in sample:
    if char != ' ' and char != ',':
        print(char, end='')