import sys

def solve():
    N = int(input())
    solutions = list(map(int, sys.stdin.readline().split()))
    solutions.sort()
    result_solution = [solutions[0], solutions[1], solutions[N - 1]]
    result_property = abs(sum(result_solution))
    for left in range(N - 2):
        mid = left + 1
        right = N - 1
        while mid < right:
            mix = solutions[left] + solutions[mid] + solutions[right]
            if result_property > abs(mix):
                result_solution = [solutions[left], solutions[mid], solutions[right]]
                result_property = abs(mix)
            if mix == 0:
                print(*result_solution)
                return
            if mix > 0:
                right -= 1
            else:
                mid += 1
    print(*result_solution)
    return

solve()