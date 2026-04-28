N = int(input())
result = 0
if N >= 100:
    for num in range(100, N + 1):
        temp = list(map(int, list(str(num))))
        if temp[0] - temp[1] == temp[1] - temp[2]:
            result += 1
    result += 99
    pass
else:
    result = N
print(result)