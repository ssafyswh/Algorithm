N, P = list(map(int, input().split()))
hand = [[] for _ in range(6)]
count = 0
for _ in range(N):
    string, fret = list(map(int, input().split()))
    string -= 1
    while hand[string] and hand[string][-1] > fret:
        hand[string].pop()
        count += 1
    if hand[string] and hand[string][-1] == fret:
        continue
    hand[string].append(fret)
    count += 1
print(count)