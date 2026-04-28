N, M = map(int, input().split())
pokedex = dict()
for i in range(1, N + 1):
    pokemon = input()
    pokedex[str(i)] = pokemon
    pokedex[pokemon] = i
for _ in range(M):
    print(pokedex[input()])