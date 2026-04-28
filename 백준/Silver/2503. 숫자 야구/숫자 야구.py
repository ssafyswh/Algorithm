N = int(input())
bench = []
check = [1] * 504
for i in range(1, 10):
    for j in range(1, 10):
        if j == i:
            continue
        for k in range(1, 10):
            if k == i or k == j:
                continue
            bench.append(str(i * 100 + j * 10 + k))
for _ in range(N):
    h, s, b = map(int, input().split())
    if s == 3:
        check = [1]
        break
    hit = str(h)
    for n in range(504):
        if check[n] == 0:
            continue
        st = 0
        bt = 0
        for m in range(3):
            if hit[m] == bench[n][m]:
                st += 1
            elif hit[m] in bench[n]:
                bt += 1
        if s != st or b != bt:
            check[n] = 0

print(sum(check))