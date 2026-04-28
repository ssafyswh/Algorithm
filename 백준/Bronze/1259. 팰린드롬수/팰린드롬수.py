while True:
    num = input()
    if num == '0':
        break
    for i in range(len(num) // 2):
        if num[i] != num[-(i+1)]:
            print('no')
            break
    else:
        print('yes')
