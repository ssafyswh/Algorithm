def queen(n=0):
    global result
    if n == N:
        result += 1
        return
    for i in range(N):
        for j in range(n):
            if chess[j] == i or chess[j] == i - (n - j) or chess[j] == i + (n - j):
                break
        else:
            chess[n] = i
            queen(n + 1)
            chess[n] = -100

N = int(input())
chess = [-100] * N
result = 0
queen()
print(result)