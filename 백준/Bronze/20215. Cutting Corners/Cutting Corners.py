h, w = map(int, input().split())
result = (h + w) - (h ** 2 + w ** 2) ** 0.5
print(result)