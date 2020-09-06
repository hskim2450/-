# N, M 입력받기
n, m = map(int, input().split())

# 청소 유무 데이터 행렬 만들기
array_clr = [[0]*m for _ in range(n)]

# r, c, d 입력받기
r, c, d = map(int, input().split())
array_clr[r][c] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보 입력받기
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

# 회전 함수
def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3

# 북, 동, 남, 서 방향설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 로봇청소기 작동
count = 1 # 맨 처음 위치 청소
turn_time = 0
while True:
  turn_left()
  nx = r + dx[d]
  ny = c + dy[d]
  if array[nx][ny] == 0 and array_clr[nx][ny] == 0:
    r = nx
    c = ny
    array_clr[r][c] = 1
    count += 1
    turn_time = 0
    continue
  else:
    turn_time += 1
    if turn_time == 4:
      nx = r - dx[d]
      ny = c - dy[d]
      if array[nx][ny] == 0:
        r = nx
        c = ny
        turn_time = 0
      else:
        break

print(count)


