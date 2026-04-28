a, b, c = list(map(int, input().split()))
if a == b:
    if b == c:
        print(f'{10000 + a * 1000}')
    else:
        print(f'{1000 + a * 100}')
elif a == c:
    if b == c:
        print(f'{10000 + a * 1000}')
    else:
        print(f'{1000 + a * 100}')
elif b == c:
    print(f'{1000 + b * 100}')
else:
    if a >= b:
        if a >= c:
            print(f'{a * 100}')
        else:
            print(f'{c * 100}')
    else:
        if b >= c:
            print(f'{b * 100}')
        else:
            print(f'{c * 100}')