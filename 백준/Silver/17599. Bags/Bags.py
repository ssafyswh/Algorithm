import sys
input = sys.stdin.readline

N = int(input())
A = [*map(int, input().split())]
bag = set()
for a in A:
    bag.add(a)
print(len(bag))