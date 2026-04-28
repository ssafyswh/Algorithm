button_time = [300, 60, 10]
T = int(input())
button_count = [0, 0, 0]
for i in range(len(button_time)):
    button_count[i] += T // button_time[i]
    T = T % button_time[i]
if T != 0:
    print(-1)
else:
    print(' '.join(list(map(str, button_count))))