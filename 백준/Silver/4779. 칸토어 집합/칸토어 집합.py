def cantor(n):
    if n == 0:
        return '-'
    return cantor(n - 1) + ' ' * 3 ** (n - 1) + cantor(n - 1)

while True:
    try:
        N = int(input())
        print(cantor(N))
    except:
        break