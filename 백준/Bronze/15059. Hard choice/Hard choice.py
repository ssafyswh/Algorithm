meal = list(map(int, input().split()))
passenger = list(map(int, input().split()))
result = 0
for i in range(3):
    if passenger[i] >= meal[i]:
        result += passenger[i] - meal[i]
print(result)