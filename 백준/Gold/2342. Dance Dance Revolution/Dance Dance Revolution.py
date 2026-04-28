import sys
# 가능한 경우의 수 2^n, n <= 10**5, 완전탐색 및 백트래킹 불가
# 처음에 구상한 dp: ddr[n][left, right][left_foot, right_foot, power_total]
# -> 실패, 사실상 dp가 아닌 greedy 해법
# 두번쩨: dp[n][left][right] = min_power_total

chart = list(map(int, sys.stdin.readline().split()))
playtime = len(chart) - 1
opposite = {(1, 3), (2, 4), (3, 1), (4, 2)}

def power(now, nxt):
    if now == nxt:
        return 1
    if now == 0:
        return 2
    if (now, nxt) in opposite:
        return 4
    return 3

MAX = 400001
ddr = [[[MAX] * 5 for _ in range(5)] for _ in range(playtime)]
first_step = chart[0]
ddr[0][first_step][0] = 2
ddr[0][0][first_step] = 2

for i in range(playtime - 1):
    step = chart[i + 1]
    for left in range(5):
        for right in range(5):
            if ddr[i][left][right] == MAX:
                continue
            power_total = ddr[i][left][right]
            if right != step:
                ddr[i + 1][step][right] = min(ddr[i + 1][step][right], power_total + power(left, step))

            if left != step:
                ddr[i + 1][left][step] = min(ddr[i + 1][left][step], power_total + power(right, step))

result = min(min(row) for row in ddr[-1])
print(result)