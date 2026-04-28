T = int(input())
for _ in range(T):
    S = input()
    stack = 0
    if len(S) % 2:
        print('NO')
        continue
    for s in S:
        if s == '(':
            stack += 1
        elif stack:
            stack -= 1
        else:
            print('NO')
            break
    else:
        if stack:
            print('NO')
        else:
            print('YES')