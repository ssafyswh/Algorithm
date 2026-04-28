import math

n = int(input())
nums = list(map(int, input().split()))
remainder = list(map(int, input().split()))
for i in range(n):
    nums[i] -= remainder[i]
    if i == 0:
        result = nums[i]
    else:
        result = math.gcd(result, nums[i])
print(result)