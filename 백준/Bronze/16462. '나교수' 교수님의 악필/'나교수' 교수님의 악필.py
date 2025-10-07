import sys

score_total = 0
N = int(input())
for _ in range(N):
    score = list(sys.stdin.readline().strip())
    for i in range(len(score)):
        if score[i] == '0' or score[i] == '6':
            score[i] = '9'
    score = int(''.join(score))
    if score > 100:
        score = 100
    score_total += score
print(int(score_total / N + 0.5))