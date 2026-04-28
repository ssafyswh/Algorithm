N = int(input())
pouch_max = N // 3
pouch_min = -1
for i in range(pouch_max + 1):
    if (N - (i * 3)) % 5 == 0:
        pouch_num = i + (N - (i * 3)) // 5
        if pouch_min == -1:
            pouch_min = pouch_num
        elif pouch_min > pouch_num:
            pouch_min = pouch_num
print(pouch_min)