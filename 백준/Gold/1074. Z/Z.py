def z(n, y=0, x=0):
    if n == 0:
        return 0
    quad = 2 ** (n - 1)
    offset = 0
    if y >= quad and x >= quad:
        offset = (quad ** 2) * 3
        y -= quad
        x -= quad
    elif y >= quad > x:
        offset = (quad ** 2) * 2
        y -= quad
    elif y < quad <= x:
        offset = quad ** 2
        x -= quad
    return offset + z(n - 1, y, x)


N, r, c = map(int, input().split())
print(z(N, r, c))