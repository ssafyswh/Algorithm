T = int(input())
for _ in range(T):
    S = input().strip()
    if S.isdigit():
        print(int(S))
    else:
        print('invalid input')