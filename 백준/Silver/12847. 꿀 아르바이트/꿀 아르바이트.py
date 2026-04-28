n, m = list(map(int, input().split()))
T = list(map(int, input().split()))
max_wage = sum(T[0 : m])
temp = max_wage
for i in range(n - m):
    temp = temp + T[m + i] - T[i]
    if max_wage < temp:
        max_wage = temp
print(max_wage)