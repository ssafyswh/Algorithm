N = int(input())
road_list = list(map(int, input().split()))
fuel_list = list(map(int, input().split()))
fuel_list.pop()
now_location = 0
move_count = 1
move_distance = 0
fuel_cost = 0
while True:
    if now_location + move_count == len(fuel_list):
        move_distance += road_list[now_location + move_count - 1]
        fuel_cost += move_distance * fuel_list[now_location]
        break
    if fuel_list[now_location] > fuel_list[now_location + move_count]:
        move_distance += road_list[now_location + move_count - 1]
        fuel_cost += fuel_list[now_location] * move_distance
        move_distance = 0
        now_location += move_count
        move_count = 1
    else:
        move_distance += road_list[now_location + move_count - 1]
        move_count += 1

print(fuel_cost)