nums = list(map(int, input().split()))
result = 0
for i in range(5):
    result += nums[i] ** 2
print(result % 10)