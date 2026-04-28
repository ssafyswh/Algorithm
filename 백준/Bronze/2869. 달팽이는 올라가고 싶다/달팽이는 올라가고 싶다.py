A, B, V = map(int, input().split())
if A >= V:
    result = 1
else:
    V -= A
    result = 1
    if V % (A - B):
        result += V // (A - B) + 1
    else:
        result += V // (A - B)
print(result)