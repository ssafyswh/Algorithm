A, B = input().split()
a = list(A)
a.reverse()
b = list(B)
b.reverse()
aa = int(''.join(a))
bb = int(''.join(b))
if aa > bb:
    print(aa)
else:
    print(bb)