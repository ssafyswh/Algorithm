a, b = list(map(int, input().split()))
c = int(input())
if b + c >= 60:
    if a + (b + c) // 60 >= 24:
        print(f'{a + (b + c) // 60 - 24} {b + c - (b + c) // 60 * 60}')
    else:
        print(f'{a + (b + c) // 60} {b + c - (b + c) // 60 * 60}')
else:
    print(f'{a} {b+c}')