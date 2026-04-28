N, K = list(map(int, input().split()))
cage_index = [0] * 1000001
polar_bear = 2 * K + 1
ice_index = [list(map(int, input().split())) for _ in range(N)]
for n in range(N):
    cage_index[ice_index[n][1]] = ice_index[n][0]
ice_max = sum(cage_index[:polar_bear])
temp = ice_max
for i in range(1000001 - polar_bear):
    temp = temp - cage_index[i] + cage_index[polar_bear + i]
    if ice_max < temp:
        ice_max = temp
print(ice_max)