budget = int(input())
watermelon = int(input())
pomegranates = int(input())
nuts = int(input())
if budget >= watermelon:
    print('Watermelon')
elif budget >= pomegranates:
    print('Pomegranates')
elif budget >= nuts:
    print('Nuts')
else:
    print('Nothing')