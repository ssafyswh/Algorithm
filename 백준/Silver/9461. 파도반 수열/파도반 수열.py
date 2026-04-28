T = int(input())
padovan = [0, 1, 1, 1, 2, 2] + [0] * 95
for i in range(6, 101):
    padovan[i] = padovan[i - 1] + padovan[i - 5]
for _ in range(T):
    N = int(input())
    print(padovan[N])