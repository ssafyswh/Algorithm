A, B, C = map(int, input().split())
result = A
if C % 2 == 1:
    result = A ^ B
print(result)