def switch(ping):
    if ping == 0:
        return 1
    else: return 0

while True:
    S = input()
    if S == '0':
        break
    time = len(S)
    satellite = list(map(int, list(S)))
    result = []
    for i in range(1, time):
        if satellite[i] == 0:
            continue
        for t in range(0, time, i):
            satellite[t] = switch(satellite[t])
        result.append(i)
    print(*result)