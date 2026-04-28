word = input().upper()
result = None
max_count = 0
count_dict = {}
for alp in word:
    if count_dict.get(alp) == None:
        count_dict[alp] = 1
    else:
        count_dict[alp] += 1
    if count_dict[alp] > max_count:
        max_count = count_dict[alp]
        result = alp
    elif count_dict[alp] == max_count:
        result = '?'
print(result)