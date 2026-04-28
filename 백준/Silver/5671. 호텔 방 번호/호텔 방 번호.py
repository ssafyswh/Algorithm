while True:
    try:
        N, M = map(int, input().split())
        result = 0
        for room in range(N, M + 1):
            if len(str(room)) == len(set(list(str(room)))):
                result += 1
        print(result)
    except:
        break