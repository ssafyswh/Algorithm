import sys

V, E = map(int, input().split())
MAX = float('inf')
distance = [[MAX] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    distance[a][b] = c

for stopover in range(1, V + 1):
    for start in range(1, V + 1):
        for goal in range(1, V + 1):
            distance[start][goal] = min(distance[start][goal], distance[start][stopover] + distance[stopover][goal])

result = min([distance[x][x] for x in range(1, V + 1)])
print(result if result != MAX else -1)