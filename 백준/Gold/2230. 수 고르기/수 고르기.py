import sys

N, M = map(int, input().split())
A = [int(sys.stdin.readline()) for _ in range(N)]
A.sort()

left = 0
right = 0
result = A[-1] - A[0]

while right < N:
    now = A[right] - A[left]
    if now > M:
        left += 1
    elif now < M:
        right += 1
    else:
        result = M
        break
    if M <= now < result:
        result = now

print(result)