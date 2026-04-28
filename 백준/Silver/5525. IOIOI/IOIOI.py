N = int(input())
M = int(input())
S = input()
count = 0
IOI = []
for i in range(M):
    if count == 0:
        if S[i] == 'I':
            count = 1
    else:
        if S[i] != S[i - 1]:
            count += 1
        elif count > 2:
            if S[i] == 'I':
                IOI.append((count - 1) // 2)
                count = 1
            else:
                IOI.append((count - 2) // 2)
                count = 0
        elif S[i] == 'I':
            count = 1
        else:
            count = 0
if count > 2:
    if S[-1] == 'I':
        IOI.append(count // 2)
    else:
        IOI.append((count - 1) // 2)
result = 0
for A in IOI:
    if A >= N:
        result += (A - N + 1)
print(result)