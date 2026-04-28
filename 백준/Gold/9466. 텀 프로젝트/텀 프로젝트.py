import sys
sys.setrecursionlimit(10**7)

def find_team(num):
    global result
    teamed[num] = 1
    team_list.append(num)
    team_set.add(num)
    student_choice = students[num]
    if teamed[student_choice]:
        if student_choice in team_set:
            while True:
                result -= 1
                if student_choice == team_list.pop():
                    break
        return
    else:
        find_team(student_choice)
    team_set.remove(student_choice)


T = int(input())
for _ in range(T):
    n = int(input())
    students = [0] + list(map(int, sys.stdin.readline().split()))
    teamed = [0] * (n + 1)
    result = n
    for i in range(1, n + 1):
        if not teamed[i]:
            team_list = []
            team_set = set()
            find_team(i)
    print(result)