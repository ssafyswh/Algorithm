def div(n1, n2):
    if n1 == 1:
        return [1]
    elif n2 > n1 / n2:
        return []
    elif n1 % n2 == 0:
        return [n2, int(n1 // n2)] + div(n1, n2 + 1)
    else:
        return div(n1, n2 + 1)

def perfect(n):
    result = sorted(div(n, 1))
    result.pop()
    if n == sum(result):
        return f'{n} = {" + ".join(list(map(str, result)))}'
    else:
        return f'{n} is NOT perfect.'

while True:
    n = int(input())
    if n == -1:
        break
    print(perfect(n))