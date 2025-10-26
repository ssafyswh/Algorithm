s1 = input()
len_s1 = len(s1)
s2 = input()
len_s2 = len(s2)

lcs_length = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
lcs_text = [[''] * (len_s2 + 1) for _ in range(len_s1 + 1)]

for y in range(1, len_s1 + 1):
    for x in range(1, len_s2 + 1):
        if s1[y-1] == s2[x-1]:
            lcs_length[y][x] = lcs_length[y-1][x-1] + 1
            lcs_text[y][x] = lcs_text[y-1][x-1] + s1[y-1]
        else:
            if lcs_length[y-1][x] > lcs_length[y][x-1]:
                lcs_length[y][x] = lcs_length[y-1][x]
                lcs_text[y][x] = lcs_text[y-1][x]
            else:
                lcs_length[y][x] = lcs_length[y][x-1]
                lcs_text[y][x] = lcs_text[y][x-1]

print(lcs_length[len_s1][len_s2])
if lcs_length[len_s1][len_s2]:
    print(lcs_text[len_s1][len_s2])