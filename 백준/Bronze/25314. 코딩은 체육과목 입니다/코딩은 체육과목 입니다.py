N = int(input())
n = int(N / 4)
ans = 'int'
for i in range(n):
    ans = 'long ' + ans
print(ans)