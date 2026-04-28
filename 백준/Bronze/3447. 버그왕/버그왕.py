def debug():
    while True:
        if len(check) >= 3 and check[-1] == 'G' and check[-2] == 'U' and check[-3] == 'B':
            for _ in range(3):
                check.pop()
        else:
            return
            
while True:
    try:
        code = list(input())
        check = []
        for i in range(len(code)):
            check.append(code[i])
            debug()
        print(''.join(check))
    except EOFError:
        break