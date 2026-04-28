import sys
import heapq

T = int(input())
for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    deleted = [0] * k
    for i in range(k):
        command, num = sys.stdin.readline().split()
        if command == 'I':
            heapq.heappush(max_heap, (-int(num), i))
            heapq.heappush(min_heap, (int(num), i))
        else:
            if num == '-1':
                while min_heap and deleted[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    number, order = heapq.heappop(min_heap)
                    deleted[order] = 1
            else:
                while max_heap and deleted[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    number, order = heapq.heappop(max_heap)
                    deleted[order] = 1
    while min_heap and deleted[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and deleted[max_heap[0][1]]:
        heapq.heappop(max_heap)
    if not min_heap:
        print('EMPTY')
    else:
        print(-max_heap[0][0], min_heap[0][0])