import sys
while True:
    A, B = map(int, sys.stdin.readline().split())
    if A or B:
        print(A + B)
    else:
        break