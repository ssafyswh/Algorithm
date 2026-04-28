def n_and_m(l=[], s=0, n=0):
    if n == M:
        print(' '.join(list(map(str, l))))
        return
    for i in range(s, N):
        l.append(nums[i])
        n_and_m(l, i+1, n + 1)
        l.pop()

        
N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
n_and_m()