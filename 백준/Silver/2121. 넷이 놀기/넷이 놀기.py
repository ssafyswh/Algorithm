import sys

N = int(input())
A, B = map(int, input().split())
dots = []
dots_set = set()
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    dots.append((x, y))
    dots_set.add((x, y))

result = 0
for i in range(N):
    dot_x, dot_y = dots[i]
    if (dot_x + A, dot_y) not in dots_set:
        continue
    if (dot_x, dot_y + B) not in dots_set:
        continue
    if (dot_x + A, dot_y + B) not in dots_set:
        continue
    result += 1
print(result)