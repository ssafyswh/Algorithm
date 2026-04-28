cost = int(input())
change = 1000 - cost
coin_count = 0
coin_list = [500, 100, 50, 10, 5, 1]
for coin in coin_list:
    coin_count += change // coin
    change = change % coin
print(coin_count)