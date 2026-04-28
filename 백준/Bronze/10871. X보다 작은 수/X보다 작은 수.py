N, X = map(int, input().split())
nums = list(map(int, input().split()))
result = []
for num in nums:
    if num < X:
        result.append(num)
print(*result)