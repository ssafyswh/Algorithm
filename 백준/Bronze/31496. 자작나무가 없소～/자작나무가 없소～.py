import sys
N, S = input().split()
result = 0
for _ in range(int(N)):
    item, nums = sys.stdin.readline().split()
    words = item.split('_')
    for word in words:
        if word == S:
            result += int(nums)
            break
print(result)