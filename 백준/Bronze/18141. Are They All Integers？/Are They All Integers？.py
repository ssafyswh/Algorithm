def integer(n, nums):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and k != i:
                    if ((nums[i] - nums[j]) / nums[k]) % 1:
                        return 'no'
    return 'yes'

n = int(input())
nums = list(map(int, input().split()))
print(integer(n, nums))