# 더 빠르고 효율적으로 풀 수 있는 방법이 있으면 좋겠다

import sys

stack = []
n = int(input()) # 명령 횟수

for i in range(n):
  s = sys.stdin.readline().split() # for문을 통한 입력은 좋지 않다는 것을 알게 됨, 앞으로 자주 사용해보면서 익혀나갈 예정
  if s[0] == 'push': # 코랩에서는 여기서 에러 발생
    stack.append(s[1])
  elif s[0] == 'pop':
    if len(stack)==0:
      print(-1)
    else:
      print(stack.pop())
  elif s[0] == 'size':
    print(len(stack))
  elif s[0] == 'empty':
    if len(stack)==0:
      print(1)
    else:
      print(0)  
  elif s[0] == 'top':
    if len(stack)==0:
      print(-1)
    else:
      print(stack[-1])
