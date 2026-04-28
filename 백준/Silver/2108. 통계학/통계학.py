import sys
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))
nums.sort()
print(round(sum(nums) / N + 0.000001))
print(nums[N // 2])
# frequency
frequency_values = []
frequency_time = 0
count = 0
for i in range(N):
    if count == 0:
        count = 1
    elif nums[i] != nums[i - 1]:
        if frequency_time < count:
            frequency_time = count
            frequency_values = [nums[i - 1]]
        elif frequency_time == count:
            frequency_values.append(nums[i - 1])
        count = 1
    else:
        count += 1
if frequency_time < count:
    frequency_time = count
    frequency_values = [nums[-1]]
elif frequency_time == count:
    frequency_values.append(nums[-1])
frequency_values.sort()
if len(frequency_values) > 1:
    print(frequency_values[1])
else:
    print(frequency_values[0])
print(nums[-1] - nums[0])