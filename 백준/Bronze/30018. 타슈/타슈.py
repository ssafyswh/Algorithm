N = int(input())
goal = list(map(int, input().split()))
now = list(map(int, input().split()))
result = 0
for i in range(N):
    result += abs(goal[i] - now[i])
print(result // 2)