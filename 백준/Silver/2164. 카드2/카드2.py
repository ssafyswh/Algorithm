import math

N = int(input())
if math.log2(N) == int(math.log2(N)):
    print(N)
else:
    bN = str(bin(N))
    result = ('0b' + bN[3:])
    print(int(result, 2) * 2)