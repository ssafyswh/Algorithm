import sys
from collections import deque

T = int(input())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    checked = [0] * 10000
    compute = deque([(A, '')])
    flag = False
    while compute:
        num, command = compute.popleft()
        D = (num * 2) % 10000
        if num > 0:
            S = num - 1
        else:
            S = 9999
        L = num // 1000 + (num % 1000) * 10
        R = num // 10 + (num % 10) * 1000
        for new_num, new_command in zip([D, S, L, R], ['D', 'S', 'L', 'R']):
            if new_num == B:
                flag = True
                result = command + new_command
                break
            if not checked[new_num]:
                compute.append((new_num, command + new_command))
                checked[new_num] = 1
        if flag:
            break
    print(result)