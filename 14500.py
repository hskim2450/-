# N, M 입력받기
n, m = map(int, input().split())

# 종이에 쓰인 수 입력받기
array =[]
for i in range(n):
  array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

max_tet = 0

# 한 point에서 계산 가능한 테트로미노 값의 최댓값 산출
def tet(x, y, d, count, sum_tet):
  def left(d):
    d -= 1
    if d == -1:
      return 3
    else:
      return d
  def right(d):
    d += 1
    if d == 4:
      return 0
    else:
      return d
  
  global array
  global dx
  global dy
  
  try:
    sum_tet += array[x][y]
    count += 1
  except:
    return 0

  if count == 4:
    return sum_tet
  elif count == 1:
    try:
      return max(sum_tet + array[x+dx[d]][y+dy[d]] + array[x+dx[left(d)]][y+dy[left(d)]] + array[x+dx[right(d)]][y+dy[right(d)]], tet(x+dx[left(d)], y+dy[left(d)], left(d), count, sum_tet), tet(x+dx[d], y+dy[d], d, count, sum_tet), tet(x+dx[right(d)], y+dy[right(d)], right(d), count, sum_tet))
    except:
      return max(tet(x+dx[left(d)], y+dy[left(d)], left(d), count, sum_tet), tet(x+dx[d], y+dy[d], d, count, sum_tet), tet(x+dx[right(d)], y+dy[right(d)], right(d), count, sum_tet))
  else:
    return max(tet(x+dx[left(d)], y+dy[left(d)], left(d), count, sum_tet), tet(x+dx[d], y+dy[d], d, count, sum_tet), tet(x+dx[right(d)], y+dy[right(d)], right(d), count, sum_tet))
  

# 모든 point에서 계산 가능한 테트로미노 값을 비교
for i in range(n):
  for j in range(m):
    max_tet = max(max_tet, tet(i, j, 0, 0, 0), tet(i, j, 1, 0, 0), tet(i, j, 2, 0, 0), tet(i, j, 3, 0, 0))

print(max_tet)
      