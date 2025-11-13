import sys

def able(limit):
    total = 0
    for delay in T:
        total += limit // delay
    if total >= M:
        return True
    return False


N, M = map(int, input().split())
T = [int(sys.stdin.readline()) for _ in range(N)]
lower = 0
upper = max(T) * M

while lower <= upper:
    mid = (lower + upper) // 2
    if able(mid):
        upper = mid - 1
    else:
        lower = mid + 1

print(lower)