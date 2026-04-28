import sys

N, M = map(int, input().split())
find = dict()
for i in range(1, N + 1):
    address, password = sys.stdin.readline().strip('\n').split()
    find[address] = password
for _ in range(M):
    print(find[sys.stdin.readline().strip('\n')])