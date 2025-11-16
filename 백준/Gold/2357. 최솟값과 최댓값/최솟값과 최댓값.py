import sys

N, M = map(int, sys.stdin.readline().split())
nums = [0] + [int(sys.stdin.readline()) for _ in range(N)]

seg = [(10**9 + 1, 0)] * (4 * N) # min, max

def init(idx, start, end):
    if start == end:
        seg[idx] = (nums[start], nums[start])
        return seg[idx]

    mid = (start + end) // 2
    left = init(idx * 2, start, mid)
    right = init(idx * 2 + 1, mid + 1, end)

    seg[idx] = (min(left[0], right[0]), max(left[1], right[1]))
    return seg[idx]

init(1, 1, N)

def query(idx, start, end, left, right):
    if start > right or end < left:
        return 10**9 + 1, 0

    if start >= left and end <= right:
        return seg[idx]

    mid = (start + end) // 2
    left_tree = query(idx * 2, start, mid, left, right)
    right_tree = query(idx * 2 + 1, mid + 1, end, left, right)
    return min(left_tree[0], right_tree[0]), max(left_tree[1], right_tree[1])

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    result = query(1, 1, N, a, b)
    print(result[0], result[1])