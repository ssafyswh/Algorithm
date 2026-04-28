N, jimin, hansoo = map(int, input().split())
tournament = list(range(1, N + 1))
result = 0
flag = False
while True:
    result += 1
    offset = N % 2
    N = N // 2 + offset
    next_round = [0] * N
    for i in range(N - offset):
        a = tournament[i * 2]
        b = tournament[i * 2 + 1]
        if (a, b) == (jimin, hansoo) or (a, b) == (hansoo, jimin):
            flag = True
            break
        if a == jimin or b == jimin:
            next_round[i] = jimin
        elif a == hansoo or b == hansoo:
            next_round[i] = hansoo
        else:
            next_round[i] = a
    if flag:
        break
    if next_round[-1] == 0:
        next_round[-1] = tournament[-1]
    tournament = next_round
print(result)