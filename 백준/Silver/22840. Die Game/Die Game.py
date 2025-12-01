def north():
    global dice2
    dice2 = dice2[1:] + [dice2[0]]
    dice1[1] = dice2[1]
    dice1[3] = dice2[3]

def east():
    global dice1
    dice1 = [dice1[3]] + dice1[:3]
    dice2[1] = dice1[1]
    dice2[3] = dice1[3]

def south():
    global dice2
    dice2 = [dice2[3]] + dice2[:3]
    dice1[1] = dice2[1]
    dice1[3] = dice2[3]

def west():
    global dice1
    dice1 = dice1[1:] + [dice1[0]]
    dice2[1] = dice1[1]
    dice2[3] = dice1[3]

while True:
    dice1 = [3, 1, 4, 6]
    dice2 = [2,
             1,
             5,
             6]
    N = int(input())
    if N == 0:
        break
    for _ in range(N):
        command = input()
        if command == 'north':
            north()
        elif command == 'east':
            east()
        elif command == 'south':
            south()
        elif command == 'west':
            west()
    print(dice1[1])
