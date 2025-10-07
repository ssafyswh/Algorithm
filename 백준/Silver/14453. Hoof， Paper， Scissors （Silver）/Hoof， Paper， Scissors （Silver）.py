import sys

N = int(input())
count_h = [0] * (N + 1)
count_p = [0] * (N + 1)
count_s = [0] * (N + 1)
for i in range(1, N + 1):
    hand = sys.stdin.readline().strip()
    count_h[i] = count_h[i - 1] + (1 if hand == 'H' else 0)
    count_p[i] = count_p[i - 1] + (1 if hand == 'P' else 0)
    count_s[i] = count_s[i - 1] + (1 if hand == 'S' else 0)
result = 0
for n in range(N + 1):
    res_h = count_h[n] + max(count_p[N] - count_p[n], count_s[N] - count_s[n])
    res_p = count_p[n] + max(count_h[N] - count_h[n], count_s[N] - count_s[n])
    res_s = count_s[n] + max(count_p[N] - count_p[n], count_h[N] - count_h[n])
    result = max(result, res_h, res_p, res_s)
print(result)