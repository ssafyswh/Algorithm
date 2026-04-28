import sys

while True:
    budget = int(sys.stdin.readline().strip())
    if not budget:
        break
    max_len = int((2 * budget) ** 0.5) + 1
    for i in range(max_len, 0, -1):
        start = ((2 * budget / i) - (i - 1)) / 2
        if start % 1 == 0 and start > 0:
            print(int(start), i)
            break