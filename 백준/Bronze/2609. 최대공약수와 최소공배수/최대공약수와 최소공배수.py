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

a, b = map(int, input().split())
A, B = a, b
primes_a = []
count_a = [0] * 10000
primes_b = []
count_b = [0] * 10000
while a > 1:
    if prime(a) == 1:
        primes_a.append(a)
        count_a[a] = 1
        break
    else:
        for i in range(2, int(a ** 0.5) + 2):
            if prime(i) == 1 and a % i == 0:
                primes_a.append(i)
                while a % i == 0:
                    a //= i
                    count_a[i] += 1
while b > 1:
    if prime(b) == 1:
        primes_b.append(b)
        count_b[b] = 1
        break
    else:
        for i in range(2, int(b ** 0.5) + 2):
            if prime(i) == 1 and b % i == 0:
                primes_b.append(i)
                while b % i == 0:
                    b //= i
                    count_b[i] += 1
gcb = 1
for prime in primes_a:
    gcb *= (prime ** min([count_a[prime], count_b[prime]]))
lcm = gcb * (A // gcb) * (B // gcb)
print(gcb)
print(lcm)