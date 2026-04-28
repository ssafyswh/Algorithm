S = input()
texts = []
for i in range(len(S)):
    texts.append(S[i:])
texts = sorted(texts)
for text in texts:
    print(text)