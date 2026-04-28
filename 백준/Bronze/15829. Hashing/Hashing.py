L = int(input())
S = input()
result = 0
for i in range(L):
    result += (31 ** i) * (ord(S[i]) - ord('a') + 1)
print(result % 1234567891)