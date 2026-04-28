def origami(N, paper):
    global minus
    global zero
    global plus
    first = paper[0][0]
    able = True
    for i in range(N):
        for j in range(N):
            if paper[i][j] != first:
                able = False
                break
        if not able:
            break
    if able:
        if first == -1:
            minus += 1
            return
        elif first == 0:
            zero += 1
            return
        else:
            plus += 1
            return
    n = N // 3
    areas = []
    for i in range(3):
        for j in range(3):
            areas.append([row[j*n:(j+1)*n] for row in paper[i*n:(i+1)*n]])
    for area in areas:
        origami(n, area)
    return

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
minus = 0
zero = 0
plus = 0
origami(N, paper)
print(minus)
print(zero)
print(plus)