text = input()
croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for alp in croatian:
    text = text.replace(alp, '*')
print(len(text))