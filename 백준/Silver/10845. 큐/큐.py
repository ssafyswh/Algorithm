import sys

N = int(input())
queue = []
count = 0
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        queue.append(command[1])
        count += 1
    elif command[0] == 'pop':
        if count:
            print(queue.pop(0))
            count -= 1
        else:
            print(-1)
    elif command[0] == 'size':
        print(count)
    elif command[0] == 'empty':
        if count:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if count:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if count:
            print(queue[-1])
        else:
            print(-1)