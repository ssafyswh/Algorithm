import sys

def check(limit):
    withdraw = 0
    wallet = 0
    for i in range(N):
        if wallet < plan[i]:
            withdraw += 1
            wallet = limit - plan[i]
        else:
            wallet -= plan[i]
    if withdraw <= M:
        return True
    return False
    
N, M = map(int, input().split())
plan = [int(sys.stdin.readline()) for _ in range(N)]
lower, upper = max(plan), 10**9 + 1
while lower <= upper:
    mid = (lower + upper) // 2
    if check(mid):
        upper = mid - 1
    else:
        lower = mid + 1
print(lower)