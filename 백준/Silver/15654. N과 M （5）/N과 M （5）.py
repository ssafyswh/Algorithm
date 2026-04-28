def n_and_m(l=[], n=0):
    if n == M:
        print(' '.join(list(map(str, l))))
        return
    for i in range(N):
        if check[i] == 1:
            continue
        check[i] = 1
        l.append(nums[i])
        n_and_m(l, n + 1)
        check[i] = 0
        l.pop()


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
check = [0] * N
n_and_m()