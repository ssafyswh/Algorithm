A, B, C = map(int, input().split())
result = 1
while B > 0:
    if B % 2 != 0:
        result = (result * A) % C
    B //= 2
    A = (A * A) % C
print(result)