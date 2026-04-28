def prime(n):
    d = 2
    if n <= 1:
        return 0
    while d ** 2 <= n:
        if n % d == 0:
            return 0
        d += 1
    else:
        return 1
N = int(input())
nums = map(int, input().split())
result = 0
for num in nums:
    result += prime(num)
print(result)