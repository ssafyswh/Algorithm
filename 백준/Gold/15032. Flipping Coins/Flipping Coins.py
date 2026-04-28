from math import factorial

N, K = map(int, input().split())

total_case = 2 ** K
cases = []
for n in range(K + 1):
    combination = factorial(K) // (factorial(K - n) * factorial(n))
    cases.append(combination)

ev_sum = 0
for i in range(K + 1):
    if i <= N:
        ev_sum += i * cases[i]
    elif (i - N) % 2:
        ev_sum += (N - 1) * cases[i]
    else:
        ev_sum += N * cases[i]

result = ev_sum / total_case
print(result)