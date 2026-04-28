N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def upper_bound(arr, x):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] <= x:
            l = mid + 1
        else:
            r = mid
    return l  # arr[l-1] ≤ x < arr[l]

ans = []
for i in range(N):
    r = upper_bound(B, A[i])
    cnt = r - (i + 1)
    if cnt < 0:
        cnt = 0
    ans.append(str(cnt))

print(" ".join(ans))