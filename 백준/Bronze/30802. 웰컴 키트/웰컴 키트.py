N = int(input())
shirts = map(int, input().split())
T, P = map(int, input().split())
result1 = 0
for size in shirts:
    if size % T == 0:
        result1 += size // T
    else:
        result1 += size // T + 1
print(result1)
print(N // P, N % P)