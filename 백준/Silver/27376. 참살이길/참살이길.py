import sys

n, k = map(int, input().split())
traffic_sign = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(k)])
time = 0
now = 0
for sign in traffic_sign:
    x, t, s = sign
    time += x - now
    now = x
    if time < s:
        time = s
    elif ((time - s) // t) % 2 == 1:
        time += t - (time - s) % t
time += n - now
print(time)