n, k = map(int, input().split())
a = list(map(int, input().split()))
result = 1
count = k
for i in range(n):
    day = a[i]
    if day > count:
       count = k
       result += 1
    count -= day
print(result)