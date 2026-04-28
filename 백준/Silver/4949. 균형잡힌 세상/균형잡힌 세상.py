while True:
    string = input()
    stack = []
    if string == '.':
        break
    for i in range(len(string)):
        if string[i] == '(' or string[i] == '[':
            stack.append(string[i])
        elif string[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                break
        elif string[i] == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break
    else:
        if stack:
            print('no')
        else:
            print('yes')