C = int(input())
for case in range(C):
    input_list = list(map(int, input().split()))
    N = input_list.pop(0)
    sum_of_score = 0
    num_of_student = 0
    for score in input_list:
        sum_of_score += score
    avg_score = sum_of_score / N
    above_avg_count = 0
    for score in input_list:
        if score > avg_score:
            above_avg_count += 1
    print('%.3f%%' % (above_avg_count / N * 100))