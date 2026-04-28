import sys

N = int(input())
stack = []
count = 0
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(command[1])
        count += 1
    elif command[0] == 'pop':
        if count:
            print(stack.pop())
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
    elif command[0] == 'top':
        if count:
            print(stack[-1])
        else:
            print(-1)