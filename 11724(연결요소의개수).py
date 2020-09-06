# 음료수 얼려먹기랑 유사한 듯
import sys

N, M = map(int, sys.stdin.readline().split())

graph = [[] for i in range(N+1)]

for i in range(M):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  graph[a].append(b)
  graph[b].append(a)
  
for i in range(N+1):
  graph[i].sort()

visited = [False] * (N+1)

def dfs(graph, v, visited):
  if not visited[v]:
    visited[v] = True
    for j in graph[v]:
      dfs(graph, j, visited)
    return True
  return False

result = 0

for i in range(1, N+1):
  if dfs(graph, i, visited):
    result += 1

print(result)