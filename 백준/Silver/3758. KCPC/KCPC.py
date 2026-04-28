import sys

T = int(input())
for _ in range(T):
    n, k, t, m = map(int, sys.stdin.readline().split())
    # 각 팀의 정보 [문제별 점수, 제출횟수, 마지막 제출]
    scores = dict()
    for team_num in range(1, n + 1):
        scores[team_num] = [[0] * (k + 1), 0, 0]
    for log_order in range(m):
        i, j, s = map(int, sys.stdin.readline().split())
        if scores[i][0][j] < s:
            scores[i][0][j] = s
        scores[i][1] += 1
        scores[i][2] = log_order
    ranking = [(sum(v[0]), v[1], v[2], k) for k, v in scores.items()]
    ranking.sort(key=lambda x: (-x[0], x[1], x[2]))
    for rank, result in enumerate(ranking, start=1):
        if result[3] == t:
            print(rank)
            break