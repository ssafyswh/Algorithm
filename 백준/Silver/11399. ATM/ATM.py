N = int(input())
withdraw_time = list(map(int, input().split()))
withdraw_time.sort()
result = 0
for i in range(N):
    result += sum(withdraw_time[: i + 1])
print(result)