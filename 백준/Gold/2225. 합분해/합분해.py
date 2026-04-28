import sys
from math import factorial

# (N + 1)H(K - 1) = (N + K - 1)C(K - 1)

N, K = map(int, sys.stdin.readline().split())
result = factorial(N + K - 1) // (factorial(N) * factorial(K - 1))
print(result % (10 ** 9))
