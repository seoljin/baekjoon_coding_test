from collections import deque
import sys

def bfs(S, T): # 점수 S와 T
  q = deque()
  q.append([S, T, 0]) # 점수 s, t, cnt = 0

  while q:
    s, t, c = q.popleft()
    # s의 점수가 더 적을 동안 반복
    if s < t:
      #공격*2, 타격+3, 발차기 횟수+1
      q.append([s * 2, t + 3, c + 1])
      #공격+1, 발차기 횟수+1
      q.append([s + 1, t, c + 1])
    
    # 점수가 동일할 때, 발차기 횟수 표시
    elif s == t:
      print(c)
      break
    
tc = int(sys.stdin.readline())
for i in range(tc):
  S, T = map(int, sys.stdin.readline().split())
  bfs(S, T)