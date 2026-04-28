from collections import deque
N, M = list(map(int, input().split()))
deq = deque(range(1, N + 1))
targets = list(map(int, input().split()))
result = 0
for target in targets:
    if deq[0] == target:
        deq.popleft()
        N -= 1
    elif deq.index(target) > (N / 2):
        while True:
            deq.rotate(1)
            result += 1
            if deq[0] == target:
                deq.popleft()
                N -= 1
                break            
    else:
        while True:
            deq.rotate(-1)
            result += 1
            if deq[0] == target:
                deq.popleft()
                N -= 1
                break
print(result)