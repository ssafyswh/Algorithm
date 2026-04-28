import sys

T = int(input())
for _ in range(T):
    N = int(input())
    left = list(map(int, sys.stdin.readline().split()))
    right = list(map(int, sys.stdin.readline().split()))
    check_left = [False] * N
    check_right = [False] * N
    timeline_left = []
    timeline_right = []
    for i in range(N):
        if check_left[i]:
            continue
        check_left[i] = True
        for j in range(i + 1, N):
            if left[i] + 500 == left[j]:
                check_left[j] = True
                timeline_left.append((left[i], left[j]))
                break
    for i in range(N):
        if check_right[i]:
            continue
        check_right[i] = True
        for j in range(i + 1, N):
            if right[i] + 500 == right[j]:
                check_right[j] = True
                timeline_right.append((right[i], right[j]))
                break
    result = 0
    for i in range(N // 2):
        for j in range(N // 2):
            if timeline_left[i][1] + 500 == timeline_right[j][0]:
                result += 1
                break
    print(result)