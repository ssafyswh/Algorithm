import sys
input = sys.stdin.readline

T, X = map(int, input().split())
N = int(input())
members = []
for _ in range(N):
    K = int(input())
    reserve = set(list(map(int, input().split())))
    members.append(reserve)

def able():
    for reservation in members:
        if X not in reservation:
            return False
    return True

if able():
    print('YES')
else:
    print('NO')