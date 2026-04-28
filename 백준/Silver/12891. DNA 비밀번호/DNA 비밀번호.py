S, P = list(map(int, input().split()))
dna_str = input()
base = ['A', 'C', 'G', 'T']
limit_list = list(map(int, input().split()))
pw_count = 0
limit_check = [0] * 4
for i in range(S - P + 1):
    if i == 0:
        temp_pw = dna_str[: P]
        for alp in temp_pw:
            limit_check[base.index(alp)] += 1
    else:
        limit_check[base.index(dna_str[i - 1])] -= 1
        limit_check[base.index(dna_str[i + P - 1])] += 1
    for n in range(4):
        if limit_check[n] < limit_list[n]:
            break
    else:
        pw_count += 1
print(pw_count)