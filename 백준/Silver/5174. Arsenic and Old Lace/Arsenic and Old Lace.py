import sys

def mix(mixture, cnt, n=0):
    global result
    if n == b:
        if mixture == poison_target:
            result = min(result, cnt)
        return
    poison = poison_list[n]
    mix(mixture, cnt, n + 1)
    mix(mixture | poison, cnt + 1, n + 1)

def parse(text):
    length = len(text)
    value = 0
    for i in range(length):
        if text[i] == 'y':
            value += 2 ** i
    return value

K = int(input())
for dataset_num in range(1, 1 + K):
    s, b = map(int, sys.stdin.readline().split())
    poison_list = []
    for _ in range(b):
        poison_list.append(parse(input()))
    poison_target = parse(input())

    result = b + 1
    mix(0, 0)
    print(f'Data Set {dataset_num}:')
    print(result if result != b + 1 else 'Impossible.')
    print()