import sys
N = int(input())
nums = [0] * 10001
for _ in range(N):
    nums[int(sys.stdin.readline())] += 1
for i in range(10001):
    while nums[i]:
        print(i)
        nums[i] -= 1