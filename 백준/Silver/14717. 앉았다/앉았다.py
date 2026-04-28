a, b = map(int, input().split())
can_lose = 0
hands = (18 * 17) // 2
if a == b:
    can_lose = 10 - a
else:
    can_lose = 0
    deck = []
    for i in range(1, 11):
        deck.append(i)
        if a == i or b == i:
            continue
        deck.append(i)
    for j in range(18):
        for k in range(j + 1, 18):
            if deck[j] == deck[k] or (deck[j] + deck[k]) % 10 >= (a + b) % 10:
                can_lose += 1

result = (hands - can_lose) / hands
print(f'{result:.3f}')