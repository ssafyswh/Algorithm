def func(x, l):
    if l == L:
        temp = int(''.join(x))
        if temp > X:
            result.append(temp)
    for i in range(L):
        if check[i] == 1:
            continue
        check[i] = 1
        func(x + [x_list[i]], l + 1)
        check[i] = 0
    return

X = int(input())
x_list = list(str(X))
L = len(x_list)
check = [0] * L
result = []
func([], 0)
if result:
    print(min(result))
else:
    print(0)