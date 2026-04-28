def inorder(n=0):
    global order
    if n >= N - 1:
        return
    inorder(n * 2 + 1)
    city[n] = buildings[order]
    order += 1
    inorder(n * 2 + 2)


K = int(input())
buildings = list(map(int, input().split()))
order = 0
N = 2 ** K
city = [0] * (N - 1)
inorder()
for k in range(K):
    print(*city[2**k-1: 2**(k+1)-1])
