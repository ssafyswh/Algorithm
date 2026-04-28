N = int(input())
result = 1
num = 1
while num < N:
    num += 6 * result
    result += 1
print(result)