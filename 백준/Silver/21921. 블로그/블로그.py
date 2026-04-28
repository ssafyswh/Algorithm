N, X = list(map(int, input().split()))
visitors = list(map(int, input().split()))
visitor_max = sum(visitors[0: X])
count_max = 1
temp = visitor_max
for i in range(N - X):
    temp = temp + visitors[X + i] - visitors[i]
    if visitor_max < temp:
        visitor_max = temp
        count_max = 1
    elif visitor_max == temp:
        visitor_max = temp
        count_max += 1
if visitor_max == 0:
    print('SAD')
else:
    print(visitor_max)
    print(count_max)