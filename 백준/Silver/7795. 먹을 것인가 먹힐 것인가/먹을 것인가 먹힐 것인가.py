from bisect import bisect_left

T = int(input())

while T:
  N,M = map(int, input().split())
  A = sorted(list(map(int, input().split())))
  B = sorted(list(map(int, input().split())))

  cnt = 0
  
  for i in A:
    cnt+=bisect_left(B,i)
  
  print(cnt)
  T -= 1