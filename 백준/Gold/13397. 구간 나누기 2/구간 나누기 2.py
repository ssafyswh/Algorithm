def able(limit):
    now = 0
    temp_min = 10001
    temp_max = 0
    for num in series:
        if num > temp_max:
            temp_max = num
        if num < temp_min:
            temp_min = num
        if temp_max - temp_min > limit:
            if now < M - 1:
                now += 1
                temp_min = num
                temp_max = num
            else:
                return False
    return True

N, M = map(int, input().split())
series = list(map(int, input().split()))
upper = max(series) - min(series)
lower = 0
while lower <= upper:
    mid = (lower + upper) // 2
    if able(mid):
        upper = mid - 1
    else:
        lower = mid + 1
print(lower)