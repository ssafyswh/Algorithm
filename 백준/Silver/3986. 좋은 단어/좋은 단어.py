N = int(input())
result = 0
for _ in range(N):
    stack = []
    word = input()
    for char in word:
        if stack and char == stack[-1]:
            stack.pop()      
        else:
            stack.append(char)
    if not stack:
        result += 1
print(result)