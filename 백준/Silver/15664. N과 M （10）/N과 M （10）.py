def n_and_m(l=[], s=0, n=0):
    global count
    if n == M:
        temp = l[:]
        results.append(temp)
        return
    for i in range(s, N):
        if check[i] == 1:
            continue
        l.append(nums[i])
        check[i] = 1
        n_and_m(l, i+1, n + 1)
        l.pop()
        check[i] = 0


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
check = [0] * N
results = []
n_and_m()
duple_check = set()
for result in results:
    if tuple(result) not in duple_check:
        duple_check.add(tuple(result))
        print(' '.join(list(map(str, result))))