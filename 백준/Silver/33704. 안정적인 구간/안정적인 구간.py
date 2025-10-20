N = int(input())
A = list(map(int, input().split()))
print('YES' if (N > 2 or A[0] <= A[1]) else 'NO')