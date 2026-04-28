N = int(input())
result = 0
for _ in range(N):
    word = input()
    appear = []
    now = ''
    for alp in word:
        if alp not in appear:
            appear.append(alp)
            now = alp
        elif now != alp:
            break
    else:
        result += 1
print(result)