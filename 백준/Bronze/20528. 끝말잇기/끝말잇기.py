N = int(input())
words = input().split()
for word in words:
    if word == words[0]:
        a = word[0]
        continue
    if word[0] != a:
        print(0)
        break
else:
    print(1)