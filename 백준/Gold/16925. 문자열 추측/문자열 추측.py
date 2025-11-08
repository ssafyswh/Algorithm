def solution(string):
    # 길이가 n인 prefix, suffix 체크
    used = [[False, False] for _ in range(N)]
    result = []
    for sub in sub_order:
        l = len(sub)
        is_prefix = (sub == S[:l])
        is_suffix = (sub == S[N - l:])
        matched = False

        if is_prefix and is_suffix:
            if not used[l][0]:
                used[l][0] = True
                result.append('P')
                matched = True
            else:
                used[l][1] = True
                result.append('S')
                matched = True
        elif is_prefix:
            used[l][0] = True
            result.append('P')
            matched = True
        elif is_suffix:
            used[l][1] = True
            result.append('S')
            matched = True

        if not matched:
            return ''

    return ''.join(result)


N = int(input())
subs = [[] for _ in range(N)]
sub_order = []
for _ in range(2 * (N - 1)):
    sub = input()
    subs[len(sub)].append(sub)
    sub_order.append(sub)

case = []
a = subs[N - 1][0]
b = subs[N - 1][1]
if a[1:] == b[:-1]:
    S1 = a + b[-1]
    case.append(S1)
if b[1:] == a[:-1]:
    S2 = b + a[-1]
    if not case or case[0] != S2:
        case.append(S2)

for S in case:
    is_correct = solution(S)
    if is_correct:
        print(S)
        print(is_correct)
        break