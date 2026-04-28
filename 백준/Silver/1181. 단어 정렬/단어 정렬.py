N = int(input())
words = [[] for _ in range(51)]
for _ in range(N):
    word = input()
    words[len(word)].append(word)
temp = ''
for i in range(1, 51):
    words[i].sort()
    for word in words[i]:
        if word != temp:
            temp = word
            print(word)