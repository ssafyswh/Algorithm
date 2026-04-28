isbn = input()
temp = 0
target = 0
for i in range(13):
    index = i + 1
    if index % 2:
        c = 1
    else:
        c = 3
    if isbn[i].isdigit():
        temp += int(isbn[i]) * c
    else:
        target = c
for j in range(10):
    if (temp + j * target) % 10 == 0:
        print(j)
        break