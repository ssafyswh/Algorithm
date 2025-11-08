def euclidean(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

N, L = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

lcm = 1
result = True
for i in range(N):
    a = A[i]
    if B[i] and lcm % a != 0:
        lcm = (lcm * a) // euclidean(lcm, a)
    if lcm > L:
        result = False
        break

if result:
    for i in range(N):
        if not B[i] and lcm % A[i] == 0:
            result = False
            break

if result and lcm <= L:
    print(lcm)
else:
    print(-1)