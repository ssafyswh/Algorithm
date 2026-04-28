N = int(input())
performers = [0] * N
for i in range(N):
    scores = list(map(int, input().split()))
    performers[i] = max(scores[:2]) + sum(sorted(scores[2:], reverse=True)[:2])
print(max(performers))