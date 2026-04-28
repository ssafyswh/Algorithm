N = int(input())
meeting_list = []
meeting_max = 0
meeting_count = 0
now_time = 0
for _ in range(N):
    a, b = list(map(int, input().split()))
    meeting_list.append([a, b])
sorted_list = sorted(meeting_list, key = lambda x : (x[1], x[0]))
init_flag = True
for meeting in sorted_list:
    if init_flag == True:
        now_time = meeting[1]
        meeting_count += 1
        init_flag = False
        continue
    if meeting[0] >= now_time:
        meeting_count += 1
        now_time = meeting[1]
print(meeting_count)