N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))
for b in B:
    start, end = 0, N - 1
    while start <= end:
        C = (start + end) // 2
        if A[C] == b:
            print(1)
            break
        elif A[C] > b:
            end = C - 1
        else:
            start = C + 1
    else:
        print(0)