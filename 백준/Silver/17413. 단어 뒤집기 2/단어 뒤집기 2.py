S = list(input())
stack = []
while len(S) > 0:
    if S[0] == '<':
        if stack:
            for _ in range(len(stack)):
                print(stack.pop(), end='')
        while S[0] != '>':
            stack.append(S.pop(0))
        stack.append(S.pop(0))
        for token in stack:
            print(token, end='')
        stack = []
    elif S[0] == ' ':
        for _ in range(len(stack)):
            print(stack.pop(), end='')
        print(S.pop(0), end='')
    else:
        stack.append(S.pop(0))
if stack:
    for _ in range(len(stack)):
        print(stack.pop(), end='')