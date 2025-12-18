import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

result = []
while True:
    cap = set(A) & set(B)
    if not cap:
        break
    value = max(cap)
    result.append(value)
    A = A[A.index(value) + 1:]
    B = B[B.index(value) + 1:]

print(len(result))
if result:
    print(*result)