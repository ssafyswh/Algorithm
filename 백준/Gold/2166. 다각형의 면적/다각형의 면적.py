import sys
input = sys.stdin.readline

N = int(input())
dots = []

for _ in range(N):
    dots.append(list(map(int, input().split())))
dots.append(dots[0])

result = 0
for i in range(N):
    result += dots[i][0] * dots[i + 1][1] - dots[i + 1][0] * dots[i][1]

print(abs(result) / 2)