import sys
input = sys.stdin.readline

N = int(input())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab_dict = {}
for i in range(N):
    for j in range(N):
        ab_sum = A[i] + B[j]
        if ab_sum in ab_dict:
            ab_dict[ab_sum] +=1
        else:
            ab_dict[ab_sum] = 1

result = 0
for i in range(N):
    for j in range(N):
        cd_sum = C[i] + D[j]
        if -cd_sum in ab_dict:
            result += ab_dict[-cd_sum]

print(result)