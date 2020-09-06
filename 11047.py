n, k = map(int, input().split())
coins = []

for i in range(n):
  coins.append(int(input()))

i = len(coins)-1
count = 0
while True:
  count += int(k/coins[i])
  k = k%coins[i]
  i -= 1
  if i == -1:
    break

print(count)