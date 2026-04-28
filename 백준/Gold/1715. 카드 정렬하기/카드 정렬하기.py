import heapq

N = int(input())
q = []
for _ in range(N):
    heapq.heappush(q, int(input()))
result = 0
while q:
    card1 = heapq.heappop(q)
    if q:
        card2 = heapq.heappop(q)
        result += card1 + card2
        heapq.heappush(q, card1 + card2)
print(result)