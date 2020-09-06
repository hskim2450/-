import sys

alphabet = [0 for i in range(26)]

n = int(sys.stdin.readline())
for i in range(n):
  # 단어 한줄 입력받기
  word = sys.stdin.readline().rstrip()
  j = 0
  # 각 단어 당 알파벳의 가중치 더하기
  while word:
    #단어 맨뒤 글자 선택
    now = word[-1]
    #가중치 더하기
    alphabet[ord(now)-ord('A')] += pow(10, j)
    #자릿수 이동
    j += 1
    #맨뒤 알파벳 제거
    word = word[:-1]

alphabet.sort(reverse=True)
sum = 0
for i in range(9,0,-1):
  sum += alphabet[9-i]*i

print(sum)
