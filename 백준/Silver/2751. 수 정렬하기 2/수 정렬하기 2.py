import sys

N = int(input())
nums = [False] * 2000001
for _ in range(N):
    num = int(sys.stdin.readline())
    nums[num + 1000000] = True
for n in range(2000001):
    if nums[n]:
        print(n - 1000000)