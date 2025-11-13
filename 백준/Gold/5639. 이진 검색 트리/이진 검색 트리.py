import sys
sys.setrecursionlimit(10**5)

preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except ValueError:
        break

def postorder(start, end):
    if start > end:
        return
    root = preorder[start]
    mid = start + 1
    while mid <= end and preorder[mid] < root:
        mid += 1
    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(root)

postorder(0, len(preorder) - 1)