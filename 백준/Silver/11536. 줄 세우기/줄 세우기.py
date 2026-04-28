N = int(input())
names = []
for _ in range(N):
    names.append(input())
increase = sorted(names)
decrease = sorted(names, reverse=True)
if names == increase:
    print('INCREASING')
elif names == decrease:
    print('DECREASING')
else:
    print('NEITHER')