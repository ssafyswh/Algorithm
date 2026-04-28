result = [-1] * 26
S = input()
for i in range(len(S)):
    if result[ord(S[i]) - ord('a')] == -1:
        result[ord(S[i]) - ord('a')] = i
print(*result)