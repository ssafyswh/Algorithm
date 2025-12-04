import sys
input = sys.stdin.readline

N = int(input())
A = [*(map(int, input().split()))]

result = 0
sum_set = set()
for i in range(1, N):
    for j in range(i - 1, -1, -1):
        temp_sum = A[i - 1] + A[j]
        sum_set.add(temp_sum)

    for j in range(i - 1, -1, -1):
        temp_diff = A[i] - A[j]
        if temp_diff in sum_set:
            result += 1
            break

print(result)