from collections import deque
import sys

N, M, V = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for i in range(N+1)]
for i in range(M):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(N+1):
  graph[i].sort()

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for j in graph[v]:
    if not visited[j]:
      dfs(graph, j, visited)

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for j in graph[v]:
      if not visited[j]:
        queue.append(j)
        visited[j] = True

visited = [False] * (N+1)

dfs(graph, V, visited)
print('')
visited = [False] * (N+1)
bfs(graph, V, visited)