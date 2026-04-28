import sys

ax, ay, az, bx, by, bz, cx, cy, cz = map(int, sys.stdin.readline().split())

ab = ((ax-bx)**2 + (ay-by)**2 + (az-bz)**2) ** 0.5

bc = ((cx-bx)**2 + (cy-by)**2 + (cz-bz)**2) ** 0.5

ca = ((ax-cx)**2 + (ay-cy)**2 + (az-cz)**2) ** 0.5

s = (ab + bc + ca) / 2

S = (s * (s-ab) * (s-bc) * (s-ca)) ** 0.5

h = S / ab * 2

if max(bc,ca) ** 2 > min(bc,ca) ** 2 + ab ** 2:

    result = min(bc, ca)

else:

    result = h

print(result)



