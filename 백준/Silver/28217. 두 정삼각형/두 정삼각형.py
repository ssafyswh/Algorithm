import sys
input = sys.stdin.readline

def calc(a, b):
    value = 0
    for i in range(N):
        for j in range(i + 1):
            if a[i][j] != b[i][j]:
                value += 1
    return value

def flip(a):
    new = []
    for i in range(N):
        new.append(a[i][::-1])
    return new

def rotate(a):
    new = [[0] * n for n in range(1, N + 1)]
    for i in range(N):
        for j in range(i + 1):
            new[N - 1 - i + j][N - 1- i]= a[i][j]
    return new

N = int(input())
A = [[*map(int, input().split())] for _ in range(N)]
B = [[*map(int, input().split())] for _ in range(N)]
result = sum(range(1, N + 1))

cases = [A, flip(A), rotate(A), flip(rotate(A)), rotate(rotate(A)), flip(rotate(rotate(A)))]
for case in cases:
    result = min(result, calc(case, B))

print(result)
