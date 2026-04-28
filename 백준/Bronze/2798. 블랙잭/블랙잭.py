def blackjack(s=0, h=0, n=0):
    if n == 3:
        result.append(s)
        return
    for i in range(h, N):
        if check[i] == 1 or s + cards[i] > M:
            continue
        s += cards[i]
        check[i] = 1
        blackjack(s, i+1, n+1)
        s -= cards[i]
        check[i] = 0

N, M = map(int, input().split())
cards = list(map(int, input().split()))
check = [0] * N
result = []
blackjack()
print(max(result))