nums = set(range(1, 31))
report = set()
for _ in range(28):
    report.add(int(input()))
result = sorted(set(nums - report))
for num in result:
    print(num)