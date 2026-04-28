canvas = [[0] * 100 for _ in range(100)]
N = int(input())
result = 0
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            canvas[i][j] = 1

result = 0
delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for i in range(100):
    for j in range(100):
        if canvas[i][j] == 1:
            check = 0
            for d in delta:
                dy = d[0] + i
                dx = d[1] + j
                if 0 <= dy < 100 and 0 <= dx < 100:
                    if canvas[dy][dx] == 1:
                        check += 1
            if check == 2:
                result += 2
            elif check == 3:
                result += 1
print(result)
