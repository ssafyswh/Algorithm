N = int(input())
deck = list(range(1, N + 1))[::-1]
graveyard = []
for _ in range(N):
    graveyard.append(deck.pop())
    if deck != []:
        bottom = deck.pop()
        deck = [bottom] + deck
print(' '.join(list(map(str, graveyard))))