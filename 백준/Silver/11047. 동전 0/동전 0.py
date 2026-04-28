N, K = list(map(int, input().split()))
coin_list = []
for _ in range(N):
    coin_input = int(input())
    coin_list = [coin_input] + coin_list
result = 0
for coin in coin_list:
    result += K // coin
    K = K % coin

print(result)