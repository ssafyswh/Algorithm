from collections import deque

def is_palindrome(text):
    for i in range(len(text) // 2):
        if text[i] != text[-(i + 1)]:
            return False
    return True


T = int(input())

for _ in range(T):
    num = int(input())
    memoization = {num}
    q = deque([(num, 0)])
    while q:
        num, turn = q.popleft()
        binary = bin(num)[2:]
        if is_palindrome(binary):
            print(turn)
            break
        if num - 1 not in memoization:
            q.append((num - 1, turn + 1))
            memoization.add(num - 1)
        if num + 1 not in memoization:
            q.append((num + 1, turn + 1))
            memoization.add(num + 1)