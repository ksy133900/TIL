from sys import stdin


n, k = map(int, stdin.readline().split())

coins = []

for _ in range(n):
    coins.append(int(stdin.readline()))

count_list = [0] * (k + 1)

count_list[0] = 1

for i in coins:
    for j in range(i, k + 1):
        count_list[j] += count_list[j - i]

print(count_list[k])