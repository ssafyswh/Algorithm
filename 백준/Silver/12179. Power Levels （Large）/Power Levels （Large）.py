T = int(input())
for case_num in range(1, 1 + T):
    D = int(input())
    if D <= 4:
        print(f'Case #{case_num}: ...')
        continue
    lower = 1
    upper = 8999
    while lower <= upper:
        mid = (lower + upper) // 2
        multi_fact = 1
        for n in range(9000, 0, -mid):
            multi_fact *= n
        if len(str(multi_fact)) < D:
            upper = mid - 1
        else:
            lower = mid + 1
    print(f"Case #{case_num}: IT'S OVER 9000{'!' * lower}")