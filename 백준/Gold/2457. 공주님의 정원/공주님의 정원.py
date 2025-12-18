import sys
input = sys.stdin.readline

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = [0] * 13
for i in range(1, 13):
    month[i] = month[i - 1] + days[i - 1]
condition1 = month[3] + 1
condition2 = month[12] + 1

N = int(input())
garden = []
for _ in range(N):
    m1, d1, m2, d2 = map(int, input().split())
    blossom = month[m1] + d1
    wither = month[m2] + d2
    garden.append((blossom, wither))
garden.sort()

def solve():
    result = 0
    last_day = condition1
    max_wither = 0
    idx = 0

    while last_day < condition2:
        flag = False
        while idx < N:
            if garden[idx][0] <= last_day:
                if garden[idx][1] > max_wither:
                    max_wither = garden[idx][1]
                    flag = True
                idx += 1
            else:
                break
        if flag:
            last_day = max_wither
            result += 1
        else:
            return 0

    if last_day < condition2:
        return 0
    else:
        return result

print(solve())