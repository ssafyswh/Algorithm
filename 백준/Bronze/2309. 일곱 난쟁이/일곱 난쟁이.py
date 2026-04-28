gnomes = []
for _ in range(9):
    gnomes.append(int(input()))
gnomes.sort()
fake_sum = sum(gnomes) - 100
flag = False
for i in range(9):
    for j in range(i + 1, 9):
        if gnomes[i] + gnomes[j] == fake_sum:
            gnomes.pop(i)
            gnomes.pop(j - 1)
            flag = True
            break
    if flag:
        break
for gnome in gnomes:
    print(gnome)