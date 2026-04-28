def solution(num):
    if num == 3:
        return 4
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return solution(num - 3) + solution(num - 2) + solution(num - 1)

T = int(input())
for _ in range(T):
    n = int(input())
    print(solution(n))
