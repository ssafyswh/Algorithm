import math

c, d = map(int, input().split())
line = input().split()
fizz = []
buzz = []
for i in range(d - c + 1):
    element = line[i]
    num = c + i
    if element == 'Fizz':
        fizz.append(num)
    elif element == 'Buzz':
        buzz.append(num)
    elif element == 'FizzBuzz':
        fizz.append(num)
        buzz.append(num)
result = [10**6, 10**6]
for f in range(len(fizz)):
    if f == 0:
        result[0] = fizz[f]
        continue
    result[0] = math.gcd(fizz[f], result[0])
for b in range(len(buzz)):
    if b == 0:
        result[1] = buzz[b]
        continue
    result[1] = math.gcd(buzz[b], result[1])
    
print(*result)