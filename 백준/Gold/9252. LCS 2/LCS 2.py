s1 = input()
len_s1 = len(s1)
s2 = input()
len_s2 = len(s2)

lcs = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

for y in range(1, len_s1 + 1):
    for x in range(1, len_s2 + 1):
        if s1[y-1] == s2[x-1]:
            lcs[y][x] = lcs[y - 1][x - 1] + 1
        else:
            if lcs[y - 1][x] > lcs[y][x - 1]:
                lcs[y][x] = lcs[y - 1][x]
            else:
                lcs[y][x] = lcs[y][x - 1]

result_text = []
y, x = len_s1, len_s2
while y > 0 and x > 0:
    if s1[y-1] == s2[x-1]:
        result_text.append(s1[y-1])
        y -= 1
        x -= 1
    elif lcs[y-1][x] > lcs[y][x-1]:
        y -= 1
    else:
        x -= 1

print(len(result_text))
if len(result_text):
    result_text.reverse()
    print(''.join(result_text))