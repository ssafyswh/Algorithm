S = 'ILOVEYONSEI'
now = input()
result = 0
for i in range(11):
    result += abs(ord(now) - ord(S[i]))
    now = S[i]
print(result)