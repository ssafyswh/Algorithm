import math

n, x = map(int, input().split())
nums = [1] * (x - n + 1)
temp = int(math.sqrt(x) + 1)
check_prime = [1] * temp
check_prime[0], check_prime[1] = 0, 0
for i in range(2, temp):
    if check_prime[i]:
        for j in range(i ** 2, temp, i):
            check_prime[j] = 0
primes = []
for i in range(2, temp):
    if check_prime[i]:
        primes.append(i)
for prime in primes:
    start = (n + prime ** 2 - 1) // (prime ** 2) * (prime ** 2)
    for j in range(start - n, x - n + 1, prime ** 2):
        nums[j] = 0
print(sum(nums))