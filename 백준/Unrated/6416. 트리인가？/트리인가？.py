import sys

flag1 = False
case_num = 0
while True:
    result = ''
    case_num += 1
    root = 0
    edges = dict()  # child: parent
    flag2 = False
    while True:
        line = list(map(int, sys.stdin.readline().split()))
        if line[-2:] == [0, 0]:
            line = line[: -2]
            flag2 = True
        if line == [-1, -1]:
            flag1 = True
            break
        for i in range(len(line) // 2):
            u, v = line[i * 2], line[i * 2 + 1]
            if edges.get(v) is None:
                edges[v] = u
            elif edges.get(v) == -1:
                edges[v] = u
                root -= 1
            else:
                result = 'not '
            if edges.get(u) is None:
                root += 1
                edges[u] = -1
        if flag2:
            break
    if flag1:
        break
    if edges == dict():
        pass
    elif root != 1:
        result = 'not '
    print(f'Case {case_num} is {result}a tree.')
