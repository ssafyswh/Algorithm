x = int(input())
n = int(input())
sum = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    sum = sum + a * b
if sum == x:
    print('Yes')
else:
    print('No')