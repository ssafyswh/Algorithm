def gcd(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    if num1 % num2 == 0:
        return num2
    return gcd(num2, num1 % num2)

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

a = a1 * b2 + a2 * b1
b = b1 * b2
k = gcd(a, b)
print(a // k, b // k)