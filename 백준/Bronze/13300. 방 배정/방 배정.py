N, K = map(int, input().split())
students =[[0] * 6 for _ in range(2)]
for _ in range(N):
    S, Y = map(int, input().split())
    students[S][Y - 1] += 1
result = 0
for s in range(2):
    for y in range(6):
        count = students[s][y]
        room = count // K
        if count % K != 0:
            room += 1
        result += room
print(result)