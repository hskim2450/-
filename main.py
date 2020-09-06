import sys
from collections import deque

def bfs(graph, start, visited, color):
  queue = deque([start])
  visited[start] = True
  color[start] = 1
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        color[i] = 3 - color[v]
      else:
        if color[i] == color[v]: #이분 그래프가 아닌 경우
          return False
  return True


K = int(input())
for i in range(K):
  V, E = map(int, sys.stdin.readline().rstrip().split())
  graph = [[] for x in range(V+1)]
  visited = [[False] for x in range(V+1)]
  color = [[0] for x in range(V+1)]
  for j in range(E):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

  result = 'YES'
  for j in range(1, E+1):
    if not visited[j]:
      if not bfs(graph, j, visited, color): # 이분그래프가 아니면
        result = 'NO'
        break
  print(result)


