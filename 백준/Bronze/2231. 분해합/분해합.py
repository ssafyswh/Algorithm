N = int(input())
for n in range(1, N):
    if n + sum(list(map(int, list(str(n))))) == N:
        print(n)
        break
else:
    print(0)