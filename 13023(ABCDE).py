import sys

N, M = map(int, sys.stdin.readline().split())

graph = [[] for i in range(N)]

for i in range(M):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  graph[a].append(b)
  graph[b].append(a)



def dfs(v, depth, visited):
    global N
    global ans
    visited[v] = True
    if depth >= 4:
      ans = True
    else:
      for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt, depth + 1, visited)
            visited[nxt] = False
    
ans = False

result = 0
for i in range(N):
  visited = [False] * N
  dfs(i, 0, visited)
  if ans:
    result = 1
    break

print(result)
  
    