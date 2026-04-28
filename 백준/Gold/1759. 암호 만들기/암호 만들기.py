def password(n=0, start=0, char='', count_c=0, count_v=0):
    if n == L :
        if count_c >= 2 and count_v >= 1:
            print(char)
        return
    for i in range(start, C):
        if letter[i] in vowel:
            password(n + 1, i + 1, char + letter[i], count_c, count_v + 1)
        else:
            password(n + 1, i + 1, char + letter[i], count_c + 1, count_v)
vowel = {'a', 'e', 'i', 'o', 'u'}
L, C = map(int, input().split())
letter = sorted(input().split())
password()