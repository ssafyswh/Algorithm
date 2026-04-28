def n_and_m(l=[], n=0):
    global count
    if n == M:
        temp = l[:]
        results.append(temp)
        return
    for i in range(N):
        l.append(nums[i])
        n_and_m(l, n + 1)
        l.pop()


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
results = []
n_and_m()
duple_check = set()
for result in results:
    if tuple(result) not in duple_check:
        duple_check.add(tuple(result))
        print(' '.join(list(map(str, result))))