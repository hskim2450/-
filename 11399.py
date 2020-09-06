# 입력
n = int(input())
min = list(map(int, input().split()))

# 오름차순 정렬 후 각 위치에서의 합 계산
min.sort()
sum = 0
for i in range(len(min)):
  for j in range(i+1):
    sum += min[j]

print(sum)