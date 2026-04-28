T = int(input())
for _ in range(T):
    N = int(input())
    one = 1
    two = 0
    for _ in range(N):
        one, two = two, one + two
    print(one, two)