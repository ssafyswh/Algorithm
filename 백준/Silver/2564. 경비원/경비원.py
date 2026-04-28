def location(direct, num):
    if direct == 1:
        return y + num
    elif direct == 2:
        return (x + y) * 2 - num
    elif direct == 3:
        return y - num
    else:
        return x + y + num

x, y = map(int, input().split())
N = int(input())
stores = []
for i in range(1, N + 1):
    compass, index = map(int, input().split())
    stores.append(location(compass, index))
n_compass, n_index = map(int, input().split())
start = location(n_compass, n_index)
result = 0
total = (x + y) * 2
for store in stores:
    temp = abs(store - start)
    if temp > total // 2:
        result += total - temp
    else:
        result += temp
print(result)
