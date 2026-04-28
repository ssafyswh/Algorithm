N = int(input())
stock = list(map(int, input().split()))
result = 0
now = 0
for i in range(N - 1, -1, -1):
    if now < stock[i]:
        now = stock[i]
    else:
        result += now - stock[i]

print(result)