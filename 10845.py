import sys
queue = []

n = int(sys.stdin.readline())
for i in range(n):
  command = list(sys.stdin.readline().rstrip().split())
  if command[0] == 'push':
    queue.append(command[1])
  elif command[0] == 'size':
    print(len(queue))
  elif command[0] == 'pop':
    try:
      print(queue[0])
      del queue[0]
    except:
      print(-1)
  elif command[0] == 'empty':
    if len(queue) == 0:
      print(1)
    else:
      print(0)
  elif command[0] == 'front':
    try:
      print(queue[0])
    except:
      print(-1)
  elif command[0] == 'back':
    try:
      print(queue[len(queue)-1])
    except:
      print(-1)

