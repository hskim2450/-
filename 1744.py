import sys

n = int(sys.stdin.readline())
nums = []
for i in range(n):
  nums.append(int(sys.stdin.readline()))

#입력받은 수 내림차순 정렬
nums.sort(reverse=True)
sum = 0

i = 0
#양수 곱셈 합산
while True:
  #수열 전체 순회 이후 break
  if i >= n:
    break
  #i번째 수가 0이하인 경우 끝
  if nums[i] <= 0:
    break
  elif i == n-1:
    sum += nums[i]
    i += 1
  #i번째 수가 1일때
  elif nums[i] == 1:
    sum += nums[i]
    i += 1
  #i번째 수가 1보다 크고, 그 다음수도 1보다 클 때
  elif nums[i+1] > 1:
    sum += nums[i]*nums[i+1]
    i += 2
  #i번째 수가 1보다 크고, 그 다음수가 1이하일 때
  else:
    sum += nums[i]
    i += 1

#음수는 뒤에서부터 순회
i = n-1
#음수 곱셈 합산
while True:
  #수열 전체 순회 이후 break
  if i < 0:
    break
  #i번째 수가 0이상인 경우 중지
  if nums[i] >= 0:
    break
  elif i == 0:
    sum += nums[i]
  #나머지(i번째 수가 음수) 중 i-1번째 수가 0이하일 경우
  elif nums[i-1] <= 0:
    sum += nums[i]*nums[i-1]
    i -= 2
  else:
    sum += nums[i]
    i -= 1

  
print(sum)