s1 = input()
s2 = input()
lcs = [[0] * len(s2) for _ in range(len(s1))]
for y in range(len(s1)):
    for x in range(len(s2)):
        if s1[y] == s2[x]:
            if x and y:
                temp = lcs[y - 1][x - 1] + 1
            else:
                temp = 1
        else:
            a, b = 0, 0
            if x:
                a = lcs[y][x - 1]
            if y:
                b = lcs[y - 1][x]
            temp = max(a, b)
        lcs[y][x] = temp
print(lcs[-1][-1])