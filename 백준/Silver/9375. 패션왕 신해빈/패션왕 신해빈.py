import sys

T = int(input())
for _ in range(T):
    n = int(input())
    fashion = dict()
    for _ in range(n):
        item, category = sys.stdin.readline().strip('\n').split()
        if fashion.get(category) is None:
            fashion[category] = [item]
        else:
            fashion[category].append(item)
    result = 1
    for key in fashion:
        result *= len(fashion[key]) + 1
    result -= 1
    print(result)