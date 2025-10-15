import sys

N = int(input())
budgets = list(map(int, sys.stdin.readline().split()))
total = int(input())
if total >= sum(budgets):
    print(max(budgets))
else:
    lower = total // N
    upper = max(budgets)
    while lower <= upper:
        mid = (lower + upper) // 2
        temp_total = 0
        for budget in budgets:
            if budget >= mid:
                temp_total += mid
            else:
                temp_total += budget
        if temp_total <= total:
            lower = mid + 1
        else:
            upper = mid - 1
    print(upper)