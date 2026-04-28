from math import factorial
N = int(input())
print(factorial(N) // (24 * factorial(N - 4)) if N > 3 else 0)