import sys

s, h = map(int, input().split())
never_seen = set()
never_seen_heard = []
count = 0
for _ in range(s):
    never_seen.add(sys.stdin.readline().strip('\n'))
for _ in range(h):
    who = sys.stdin.readline().strip('\n')
    if who in never_seen:
        count += 1
        never_seen_heard.append(who)
never_seen_heard.sort()
print(count)
for who in never_seen_heard:
    print(who)