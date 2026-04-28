N = int(input())
nums = list(map(int, input().split()))
sums = [0]
for i in range(N):
    if nums[i] >= 0:
        if sums[-1] < 0:
            sums.append(nums[i])
        else:
            sums[-1] += nums[i]
    else:
        if sums[-1] <= 0:
            sums[-1] += nums[i]
        else:
            sums.append(nums[i])
for i in range(1, len(sums)):
    if sums[i - 1] > 0 and sums[i - 1] + sums[i] > 0:
        sums[i] = sums[i - 1] + sums[i]
result = max(sums)
if result < 0:
    result = max(nums)
print(result)
