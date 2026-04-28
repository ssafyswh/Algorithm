import sys

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def recur(n, k=0):
    global result
    if n == M:
        temp_sum = 0
        for house in houses:
            sy, sx = house
            temp_sum += distance(sy, sx)
            if temp_sum >= result:
                return
        result = temp_sum
        return
    for i in range(k, count_chicken):
        chicken = chickens[i]
        if not closed[i]:
            closed[i] = 1
            city[chicken[0]][chicken[1]] = 0
            recur(n - 1, i + 1)
            closed[i] = 0
            city[chicken[0]][chicken[1]] = 2

def distance(sy, sx):
    value = 2000
    for i in range(count_chicken):
        if not closed[i]:
            dist = abs(chickens[i][0] - sy) + abs(chickens[i][1] - sx)
            value = min(value, dist)
    return value

N, M = map(int, input().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
houses = []
chickens = []
for y in range(N):
    for x in range(N):
        if city[y][x] == 1:
            houses.append((y, x))
        elif city[y][x] == 2:
            chickens.append((y, x))
count_house, count_chicken = len(houses), len(chickens)
result = N * 2 * count_house
closed = [0] * count_chicken
recur(count_chicken)
print(result)