N = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(list(set(nums)))
index = dict()
for i in range(len(sorted_nums)):
    index[sorted_nums[i]] = i
print(*[index[i] for i in nums])