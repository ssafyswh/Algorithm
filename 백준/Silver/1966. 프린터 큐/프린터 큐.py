T = int(input())
for case_num in range(1, T + 1):
    N, target = list(map(int, input().split()))
    docs = list(map(int, input().split()))
    now_max = max(docs)
    count = 0
    while count != N:
        if docs[0] == now_max:
            docs.pop(0)
            count += 1
            if target == 0:
                break
            else:
                target -= 1
            now_max = max(docs)
        else:
            docs = docs[1:] + [docs[0]]
            if target == 0:
                target = len(docs) - 1
            else:
                target -= 1
    result = count
    print(result)