initial = {'B': 0, 'C': 1, 'M': 2, 'W': 3}
animals = ['Bobcat', 'Coyote', 'Mountain Lion', 'Wolf']

T = int(input())
for _ in range(T):
    count = [0, 0, 0, 0]
    location, species = input().split()
    for s in species:
        count[initial[s]] += 1
    dominant = [count[0] * 2, count[1], count[2] * 4, count[3] * 3]
    result = [0, []]
    for i in range(4):
        if dominant[i] > result[0]:
            result[0] = dominant[i]
            result[1] = [i]
        elif dominant[i] == result[0]:
            result[1].append(i)
    if len(result[1]) == 1:
        print(f'{location}: The {animals[result[1][0]]} is the dominant species')
    else:
        print(f'{location}: There is no dominant species')