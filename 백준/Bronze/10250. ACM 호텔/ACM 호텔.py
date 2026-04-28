T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    x, y = str((N - 1) // H + 1), str((N - 1) % H + 1)
    if len(x) == 1:
        result = y + '0' + x
    else:
        result = y + x
    print(result)