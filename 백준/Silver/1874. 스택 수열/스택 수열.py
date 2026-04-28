N = int(input())
stack = []
now = 0
result = []
possible = True

for _ in range(N):
    num = int(input())
    if num > now:
        for i in range(now + 1, num + 1):
            stack.append(i)
            result.append('+')
        now = num
        stack.pop()
        result.append('-')
    else:
        if stack and stack[-1] == num:
            stack.pop()
            result.append('-')
        else:
            possible = False
            break
if possible and not stack:
    for command in result:
        print(command)
else:
    print('NO')