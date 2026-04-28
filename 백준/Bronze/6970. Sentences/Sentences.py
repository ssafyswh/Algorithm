T = int(input())
for _ in range(T):
    s = int(input())
    v = int(input())
    o = int(input())
    subject = [input() for _ in range(s)]
    verb = [input() for _ in range(v)]
    object = [input() for _ in range(o)]
    for i in range(s):
        for j in range(v):
            for k in range(o):
                print(f'{subject[i]} {verb[j]} {object[k]}.')
    print()