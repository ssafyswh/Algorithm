n = int(input())
f = [0, 1]

for _ in range(n - 1):
    f.append(f[-1] + f[-2])
print(f[n])