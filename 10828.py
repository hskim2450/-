# 이 문제에서는 sys.stdin.readline().rstrip().split() 사용해야 한다(시간초과문제 때문)
import sys
stack = []

n = int(sys.stdin.readline())
for i in range(n):
  command = list(sys.stdin.readline().rstrip().split())
  if command[0] == 'push':
    stack.append(command[1])
  elif command[0] == 'top':
    try:
      print(stack[len(stack)-1])
    except:
      print(-1)
  elif command[0] == 'size':
    print(len(stack))
  elif command[0] == 'pop':
    try:
      print(stack[len(stack)-1])
      stack.pop()
    except:
      print(-1)
  elif command[0] == 'empty':
    if len(stack) == 0:
      print(1)
    else:
      print(0)
