import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())
MAX = 2000000
min_S, max_S = MAX, 1
dots = []
for _ in range(N):
    r, c, S = map(int, input().split())
    dots.append((r, c, S))
    min_S = min(min_S, S)
    max_S = max(max_S, S)

def solve():
    max_result = max_S - min_S
    result = 0
    for i in range(N):
        r1, c1, S1 = dots[i]
        for j in range(i + 1, N):
            r2, c2, S2 = dots[j]
            if abs(r1 - r2) > A - 1:
                continue
            if abs(c1 - c2) > B - 1:
                continue
            result = max(result, abs(S1 - S2))
            if result == max_result:
                return result
    return result

print(solve())