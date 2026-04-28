stick = list(map(int, input().split()))
stick.sort()
a, b, c = stick
if a + b <= c:
    c = a + b - 1
print(a + b + c)