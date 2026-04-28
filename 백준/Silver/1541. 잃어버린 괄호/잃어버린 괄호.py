sample = list(input())
degrees = []
number = ''
for char in sample:
    if char.isdigit() is True:
        number = number + char
    else:
        degrees.append(number)
        number = ''
        degrees.append(char)
degrees.append(number)

init_flag = True
minus_encounter = 1
result = 0
for degree in degrees:
    if init_flag == True:
        result += int(degree)
        init_flag = False
        continue
    if degree == '+':
        continue
    elif degree == '-':
        minus_encounter = -1
    else:
        result += (minus_encounter * int(degree))

print(result)