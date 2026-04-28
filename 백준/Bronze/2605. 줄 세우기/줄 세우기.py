N = int(input())
nums = list(map(int, input().split()))
row = []
for i in range(N):
    student = i + 1
    row.insert(student - nums[i] - 1, student)
print(*row)