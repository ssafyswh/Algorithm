K = int(input())
ledger = []
for _ in range(K):
    num = int(input())
    if num:
        ledger.append(num)
    else:
        ledger.pop()
print(sum(ledger))