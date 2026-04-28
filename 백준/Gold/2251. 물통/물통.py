from collections import deque

def pour(give, take, limit):
    if give + take <= limit:
        return 0, give + take
    return give + take - limit ,limit

A, B, C = map(int, input().split())
limits = [A, B, C]
visited = [False] * (C + 1)
start = (0, 0, C)
memoization = {start}
q = deque([start])

while q:
    state = q.popleft()
    if state[0] == 0:
        visited[state[2]] = True

    # i -> j
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            if state[i] == 0 or state[j] == limits[j]:
                continue
            new_state = list(state)
            new_i, new_j = pour(state[i], state[j], limits[j])
            new_state[i], new_state[j] = new_i, new_j
            new_state = tuple(new_state)
            if new_state not in memoization:
                q.append(new_state)
                memoization.add(new_state)

result = []
for i in range(C + 1):
    if visited[i]:
        result.append(i)
print(*result)