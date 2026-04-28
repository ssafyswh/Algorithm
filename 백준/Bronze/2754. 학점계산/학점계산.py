grade = input()
while True:
    if grade[0] == 'A':
        result = 4
    elif grade[0] == 'B':
        result = 3
    elif grade[0] == 'C':
        result = 2
    elif grade[0] == 'D':
        result = 1
    else:
        result = float(0)
        break
    if grade[1] == '+':
        result += 0.3
    elif grade[1] == '-':
        result -= 0.3
    break
print(float(result))