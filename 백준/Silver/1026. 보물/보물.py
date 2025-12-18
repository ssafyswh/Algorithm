import sys
input = sys.stdin.readline

N = int(input())
A = [*map(int, input().split())]
B = [*map(int, input().split())]
A.sort()
B.sort()
B.reverse()
result = 0
for i in range(N):
    result += A[i] * B[i]
print(result)