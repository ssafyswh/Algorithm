for i in range(3):
    S = input()
    if S.isdigit():
        result = int(S) + (3 - i)
if result % 3 == 0 and result % 5 == 0:
    print('FizzBuzz')
elif result % 3 == 0:
    print('Fizz')
elif result % 5 == 0:
    print('Buzz')
else:
    print(result)