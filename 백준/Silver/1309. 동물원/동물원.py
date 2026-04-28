N = int(input())
lion = [1] * 3
for _ in range(1, N):
    lion[0], lion[1], lion[2] = sum(lion) % 9901, (lion[0] + lion[2]) % 9901, (lion[0] + lion[1]) % 9901

print(sum(lion) % 9901)