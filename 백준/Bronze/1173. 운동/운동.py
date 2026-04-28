N, m, M, T, R = map(int, input().split())
result = 0
X = m
if M - m < T:
    result = -1
else:
    while N > 0:
        result += 1
        if X + T <= M:
            X += T
            N -= 1
        else:
            X -= R
            if X < m:
                X = m
print(result)