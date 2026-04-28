N, M = map(int, input().split())
for _ in range(N):
    array = list(input())
    print(''.join(array[::-1]))