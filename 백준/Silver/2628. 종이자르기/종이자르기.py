width, height = map(int, input().split())
N = int(input())
paper = [(0, 0, height, width)]  # y1, x1, y2, x2
for _ in range(N):
    direct, index = map(int, input().split())
    for i in range(len(paper)):
        y1, x1, y2, x2 = paper[i]
        if direct == 0:
            if y1 < index < y2:
                paper[i] = (y1, x1, index, x2)
                paper.append((index, x1, y2, x2))
        elif direct == 1:
            if x1 < index < x2:
                paper[i] = (y1, x1, y2, index)
                paper.append((y1, index, y2, x2))
for i in range(len(paper)):
    y1, x1, y2, x2 = paper[i]
    paper[i] = (y2 - y1) * (x2 - x1)
print(max(paper))