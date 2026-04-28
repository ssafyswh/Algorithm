T = int(input())
for _ in range(T):
    keylog = input()
    result1 = []
    result2 = []
    count1 = 0
    count2 = 0
    for log in keylog:
        if log == '<':
            if result1:
                result2.append(result1.pop())
        elif log == '>':
            if result2:
                result1.append(result2.pop())
        elif log == '-':
            if result1:
                result1.pop()
        else:
            result1.append(log)
    print(''.join(result1) + ''.join(result2[::-1]))