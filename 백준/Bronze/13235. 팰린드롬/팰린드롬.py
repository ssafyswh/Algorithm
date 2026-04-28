S = input()
for i in range(len(S) // 2):
    if S[i] != S[-(i + 1)]:
        print('false')
        break
else:
    print('true')