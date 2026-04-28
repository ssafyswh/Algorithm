word, bomb = input(), input()
L = len(bomb)
temp = list(bomb)
count = 0
stack = []
for letter in word:
    stack.append(letter)
    count += 1
    if count >= L and letter == bomb[-1]:
        for i in range(L):
            if temp[-(i + 1)] != stack[-(i + 1)]:
                break
        else:
            for _ in range(L):
                stack.pop()
            count -= L
result = ''.join(stack)
if result:
    print(result)
else:
    print('FRULA')