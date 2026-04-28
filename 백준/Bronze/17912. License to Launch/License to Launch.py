N = int(input())
junks = list(map(int, input().split()))
result = 0
min_junk = junks[0]
for i in range(N):
    if min_junk > junks[i]:
        min_junk = junks[i]
        result = i
print(result)