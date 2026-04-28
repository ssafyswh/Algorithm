K = int(input())
points = []
y, x = (0, 0)
for _ in range(6):
    direction, distance = map(int, input().split())
    if direction == 1:
        x += distance
    elif direction == 2:
        x -= distance
    elif direction == 3:
        y += distance
    elif direction == 4:
        y -= distance
    points.append((y, x))
y_index = set()
x_index = set()
for i in range(6):
    y_index.add(points[i][0])
    x_index.add(points[i][1])
y_index = sorted(list(y_index))
x_index = sorted(list(x_index))
big_square = [(y_index[0], x_index[0]), (y_index[0], x_index[2]), (y_index[2], x_index[0]), (y_index[2], x_index[2])]
for point in big_square:
    for point2 in points:
        if point == point2:
            break
    else:
        target = point
        break
target_y, target_x = target[0], target[1]
area = (x_index[2] - x_index[0]) * (y_index[2] - y_index[0]) - abs(x_index[1] - target_x) * abs(y_index[1] - target_y)
print(area * K)