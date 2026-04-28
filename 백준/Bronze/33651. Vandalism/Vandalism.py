uapc = ['U', 'A', 'P', 'C']
sample = list(input())
for char in sample:
    uapc.remove(char)
print(''.join(uapc))