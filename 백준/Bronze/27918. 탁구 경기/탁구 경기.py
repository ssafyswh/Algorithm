import sys
N = int(input())
D, P = 0, 0
for _ in range(N):
    predict = sys.stdin.readline().strip('\n')
    if predict == 'D':
        D += 1
    else:
        P += 1
    if abs(D - P) == 2:
        break
print(f'{D}:{P}')