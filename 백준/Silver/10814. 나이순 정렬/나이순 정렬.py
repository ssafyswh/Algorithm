import sys
N = int(input())
member = dict()
for _ in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    if member.get(age) is None:
        member[age] = [name]
    else:
        member[age].append(name)
result = sorted(member.items())
for user in result:
    for name in user[1]:
        print(user[0], name)