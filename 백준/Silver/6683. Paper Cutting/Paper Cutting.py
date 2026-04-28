import sys

while True:
    a, b, c, d, e, f = map(int, sys.stdin.readline().split())
    if (a, b, c, d, e, f) == (0, 0, 0, 0, 0, 0):
        break
    if a * b * c * d > e * f:
        print('The paper is too small.')
        continue
    cuts = 10 ** 6 + 1
    if a * c <= e and b * d <= f:
        cuts_1 = a * b - 1
        cuts_1 += (1 if e - a * c else 0) + (1 if f - b * d else 0)
        cuts = min(cuts, cuts_1)

    if a * c <= f and b * d <= e:
        cuts_2 = a * b - 1
        cuts_2 += (1 if f - a * c else 0) + (1 if e - b * d else 0)
        cuts = min(cuts, cuts_2)

    if a * d <= e and b * c <= f:
        cuts_3 = a * b - 1
        cuts_3 += (1 if e - a * d else 0) + (1 if f - b * c else 0)
        cuts = min(cuts, cuts_3)

    if a * d <= f and b * c <= e:
        cuts_4 = a * b - 1
        cuts_4 += (1 if f - a * d else 0) + (1 if e - b * c else 0)
        cuts = min(cuts, cuts_4)

    if cuts != 10 ** 6 + 1:
        print(f'The minimum number of cuts is {cuts}.')
    else:
        print('The paper is too small.')