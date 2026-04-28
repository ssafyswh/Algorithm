import sys

N = int(input())
result = 0
survey = []
for _ in range(N):
    survey.append(int(sys.stdin.readline()))
survey.sort()
cut = int(N * 0.15 + 0.5)
if N - cut * 2 > 0:
    if cut == 0:
        result = int(sum(survey) / N + 0.5)
        print(result)
    else:
        result = int(sum(survey[cut: -cut]) / (N - cut * 2) + 0.5)
        print(result)
else:
    print(0)