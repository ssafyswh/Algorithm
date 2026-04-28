import sys
input = sys.stdin.readline
from math import gcd

mod = 10 ** 9 + 7
result = 0

def multi(a, b):
    if b == 1:
        return a
    if b % 2:
        return a * multi(a, b - 1) % mod
    c = multi(a, b // 2)
    return c ** 2 % mod

M = int(input())
for _ in range(M):
    N, S = map(int, input().split())
    g = gcd(N, S)
    N //= g
    S //= g

    result += S * multi(N, mod - 2) % mod
    result %= mod

print(result)
