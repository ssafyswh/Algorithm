def binary(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    return binary(n // 2) + str(n % 2)

print(binary(int(input())))