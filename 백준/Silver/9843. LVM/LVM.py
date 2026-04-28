import sys

N = int(input())
stack = []
store = None
commands = [sys.stdin.readline().split() for _ in range(N)]
order = 0
while order < N:
    command = commands[order]
    if command[0] == 'PUSH':
        stack.append(int(command[1]))
    elif command[0] == 'STORE':
        store = stack.pop()
    elif command[0] == 'LOAD':
        stack.append(store)
    elif command[0] == 'PLUS':
        stack.append(stack.pop() + stack.pop())
    elif command[0] == 'TIMES':
        stack.append(stack.pop() * stack.pop())
    elif command[0] == 'IFZERO':
        if stack.pop() == 0:
            order = int(command[1])
            continue
    elif command[0] == 'DONE':
        print(stack[-1])
        break
    
    order += 1