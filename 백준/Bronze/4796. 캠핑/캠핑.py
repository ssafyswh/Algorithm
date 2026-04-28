case_num = 0
while True :
    case_num += 1
    L, P, V = list(map(int, input().split()))
    if [L, P, V] == [0, 0, 0]:
        break
    camp_days = 0
    rest_of_days = V
    while True:
        if rest_of_days > P:
            rest_of_days -= P
            camp_days += L
        elif rest_of_days == P:
            camp_days += L
            break
        else:
            if rest_of_days <= L:
                camp_days += rest_of_days
                break
            else:
                camp_days += L
                break
    print(f'Case {case_num}: {camp_days}')