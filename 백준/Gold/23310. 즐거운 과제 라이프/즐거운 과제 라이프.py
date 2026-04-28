import sys
input = sys.stdin.readline
import math

N, M = map(int, input().split())
report = [*map(int, input().split())]

result_day = float('inf')
result_idx = -1

for i in range(1, N + 1):
    Xi = report[i - 1]
    g = math.gcd(N, M)
    if i % g != 0:
        final_k = Xi - 1
    else:
        T = M // g
        work_per_cycle = T - 1
        if work_per_cycle == 0:
            continue

        num_cycles = (Xi - 1) // work_per_cycle
        remain = (Xi - 1) % work_per_cycle + 1

        ng = N // g
        ig = i // g
        mod_val = M // g
        k_rest = -1
        for k_cand in range(mod_val):
            if (k_cand * ng) % mod_val == (-ig) % mod_val:
                k_rest = k_cand
                break

        if remain <= k_rest:
            final_k = num_cycles * T + (remain - 1)
        else:
            final_k = num_cycles * T + remain

    finish_day = i + final_k * N
    if finish_day < result_day:
        result_day = finish_day
        result_idx = i

print(result_idx)