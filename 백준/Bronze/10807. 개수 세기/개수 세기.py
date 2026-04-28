N = int(input())
nums = list(map(int, input().split()))
v = int(input())
result = 0
for num in nums:
    if num == v:
        result += 1
print(result)