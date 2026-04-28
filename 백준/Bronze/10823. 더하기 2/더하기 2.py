S = ''
while True:
    try:
        S = S + input()
    except:
        result = sum(list(map(int, S.split(','))))
        print(result)
        break