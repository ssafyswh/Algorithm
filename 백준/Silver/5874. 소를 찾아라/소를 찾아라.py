S = input()
hind = 0
result = 0
for i in range(len(S) - 1):
    if S[i] == '(' and S[i] == S[i + 1]:
        hind += 1
    if S[i] == ')' and S[i] == S[i + 1]:
        result += hind
print(result)