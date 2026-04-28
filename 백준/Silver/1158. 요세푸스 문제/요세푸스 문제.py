N, K = list(map(int, input().split()))
circle_table = list(range(1, N+1))
rest_people = N
ready_to_remove = 0
target = -1
count = 0
result = []
while True:
    target += 1
    if target == rest_people:
        for _ in range(ready_to_remove):
            circle_table.remove(0)
        target = 0
        rest_people -= ready_to_remove
        ready_to_remove = 0
        if rest_people == 0:
            break
    if circle_table[target] != 0:
        count += 1
    if count == K:
        result.append(circle_table[target])
        circle_table[target] = 0
        ready_to_remove += 1
        count = 0
print(f'<{", ".join(list(map(str, result)))}>')