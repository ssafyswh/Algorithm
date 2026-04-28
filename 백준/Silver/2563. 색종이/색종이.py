canvas = [[0] * 100 for _ in range(100)]
p = int(input())
for _ in range(p):
    x_co, y_co = list(map(int, input().split()))
    for x in range(x_co, x_co + 10):
        for y in range(y_co, y_co + 10):
            canvas[x][y] += 1

paper_count = 0
for x in range(100):
    for y in range(100):
        if canvas[x][y] != 0:
            paper_count += 1
print(paper_count)