vowel = {'a', 'e', 'i', 'o', 'u'}
alp = [chr(x) for x in range(ord('a'), ord('z') + 1)]

N = int(input())
name = []
cnt = 0

def make_name():
    global cnt, N
    if cnt >= N:
        return
    length = len(name)
    if 3 <= length <= 20:
        print(''.join(name))
        cnt += 1
        if cnt >= N:
            return
    if length > 20:
        return
    
    for i in range(26):
        if length < 2:
            pass
        elif name[-1] in vowel and name[-2] in vowel and alp[i] in vowel:
            continue
        elif name[-1] not in vowel and name[-2] not in vowel and alp[i] not in vowel:
            continue
        name.append(alp[i])
        make_name()
        name.pop()
        
make_name()