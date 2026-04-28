import sys

def binary_search(lower, upper, num):
    while lower < upper:
        mid = (lower + upper) // 2
        if lis[mid] < num:
            lower = mid + 1
        else:
            upper = mid
    return upper


N = int(input())
A = list(map(int, input().split()))
lis = [A[0]]

for i in range(1, N):
    if lis[-1] < A[i]:
        lis.append(A[i])
    else:
        pos = binary_search(0, len(lis), A[i])
        lis[pos] = A[i]

print(len(lis))