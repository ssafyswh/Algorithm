def switch(n):
    if switches[n] == 1:
        switches[n] = 0
    else:
        switches[n] = 1
    return


N = int(input())
switches = [-216] + list(map(int, input().split()))
M = int(input())
for _ in range(M):
    gender, num = map(int, input().split())
    # gender: 1은 남학생 2는 여학생
    if gender == 1:
        for i in range(1, N // num + 1):
            switch(i * num)
    elif gender == 2:
        start, end = num, num
        while True:
            if start > 1 and end < N:
                if switches[start - 1] == switches[end + 1]:
                    start -= 1
                    end += 1
                else:
                    break
            else:
                break
        for j in range(start, end + 1):
            switch(j)
for k in range(N // 20):
    print(*switches[k * 20 + 1: (k + 1) * 20 + 1])
print(*switches[(N // 20) * 20 + 1:])