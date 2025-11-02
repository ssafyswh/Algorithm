N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
result = 0
for a in A:
    if a > B:
        result += (a - B) // C + (1 if (a - B) % C else 0)
    result += 1
print(result)