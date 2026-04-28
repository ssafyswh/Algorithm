M, N = map(int, input().split())
prime = [1] * (N + 1)
prime[0: 2] = [0, 0]
for i in range(2, N + 1):
    if prime[i]:
        for j in range(i, N + 1, i):
            prime[j] = 0
        if i >= M:
            print(i)