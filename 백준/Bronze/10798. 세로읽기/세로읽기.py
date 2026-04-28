max_length = 0
word_matrix = []
for i in range(5):
    word_matrix.append(list(input()))
    if len(word_matrix[i]) > max_length:
        max_length = len(word_matrix[i])
for j in range(5):
    if len(word_matrix[j]) < max_length:
        for _ in range(max_length - len(word_matrix[j])):
            word_matrix[j].append('')
for x in range(max_length):
    temp_list = []
    for y in range(5):
        temp_list.append(word_matrix[y][x])
    print(''.join(temp_list), end='')