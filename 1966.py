import sys

t = int(sys.stdin.readline())

# 큐에서 순서 바뀔때마다 조정되는 m의 위치
def m_move():
  global m
  global doc_len
  m -= 1
  if m == -1:
    m = doc_len-1

for i in range(t):
  n, m = map(int, sys.stdin.readline().rstrip().split())
  docs = list(map(int, sys.stdin.readline().rstrip().split()))
  doc_len = n
  # 프린트 한 횟수
  count = 0
  while True:
    # 이중 반복문을 제어하기 위한 더블브레이크
    doublebreak = False
    # 큐의 맨 처음 수가 제일 큰지 비교
    for j in range(doc_len):
      # 첫 수보다 큰 수가 있을 경우 위치조정, m의 위치조정
      if docs[j] > docs[0]:
        memo = docs[0]
        del docs[0]
        docs.append(memo)
        m_move()
        break
      # 다 순회했을 때 첫 수보다 큰 수가 없을 경우
      elif j == doc_len-1:
        # 첫수가 궁금한 숫자인 경우
        if m == 0:
          count += 1
          print(count)
          doublebreak = True
          break
        # 그 외 숫자가 첫 수인 경우
        else:
          del docs[0]
          m_move()
          count += 1
    if doublebreak:
      break
    else:
      doc_len = len(docs)

    
    




