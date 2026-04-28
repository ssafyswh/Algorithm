from collections import deque

import sys

T = int(input())
for _ in range(T):
    commands = input()
    n = int(sys.stdin.readline())
    li = list(input().split(','))
    if li[0][0] == '[':
        li[0] = li[0][1:]
        if li[0] == '':
            li.pop(0)
    if li[-1][-1] == ']':
        li[-1] = li[-1][:-1]
    if li == ['']:
        li.pop()
    dq = deque(li)
    reverse = 1
    flag = False
    for command in commands:
        if command == 'R':
            reverse *= -1
        else:
            if not dq:
                print('error')
                flag = True
                break
            elif reverse == 1:
                dq.popleft()
            else:
                dq.pop()
    if flag:
        continue
    if reverse == 1:
        print('[' + ','.join(list(dq)) + ']')
    else:
        print('[' + ','.join(list(dq)[::-1]) + ']')