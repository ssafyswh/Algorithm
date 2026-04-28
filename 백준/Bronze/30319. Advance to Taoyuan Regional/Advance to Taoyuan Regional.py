year, month, date = map(int, input().split('-'))
if month < 9:
    print('GOOD')
elif month == 9:
    if date <= 16:
        print('GOOD')
    else:
        print('TOO LATE')
else:
    print('TOO LATE')