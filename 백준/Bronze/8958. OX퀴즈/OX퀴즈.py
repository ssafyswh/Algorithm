T = int(input())
for t in range(T):
    correct_list = list(input())
    score_now = 0
    score_sum = 0
    for correct in correct_list:
        if correct is 'O':
            score_now += 1
            score_sum += score_now
        else:
            score_now = 0
    print(score_sum)