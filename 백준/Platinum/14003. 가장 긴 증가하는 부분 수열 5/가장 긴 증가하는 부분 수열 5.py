import sys
input = sys.stdin.readline

def get_lis(A):
    lis = [A[0]]
    idx = [-1] * N
    prev = [-1] * N

    idx[0] = 0

    for i in range(1, N):
        curr_val = A[i]
        if curr_val > lis[-1]:
            prev[i] = idx[len(lis) - 1]
            idx[len(lis)] = i
            lis.append(curr_val)

        else:
            lower = 0
            upper = len(lis)
            pos = upper
            while lower < upper:
                mid = (lower + upper) // 2
                if lis[mid] < curr_val:
                    lower = mid + 1
                else:
                    pos = mid
                    upper = mid
            lis[pos] = curr_val
            idx[pos] = i

            if pos > 0:
                prev[i] = idx[pos - 1]
    max_len = len(lis)
    lis_end_index = idx[max_len - 1]
    return max_len, prev, lis_end_index

def backtrace(prev, lis_end_index, A):
    lis = []
    curr_idx = lis_end_index
    while curr_idx != -1:
        lis.append(A[curr_idx])
        curr_idx = prev[curr_idx]

    return lis[::-1]



N = int(input())
A = list(map(int, input().split()))

m, p, e = get_lis(A)
print(m)
print(*backtrace(p, e, A))