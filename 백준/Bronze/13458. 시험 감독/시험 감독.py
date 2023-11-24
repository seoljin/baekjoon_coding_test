from math import ceil

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for i in range(N):
  # 총 감독관은 N명 
  # 부 감독관은 c*x
  num = A[i]-B
  if num>0:
    answer += ceil(num/C)
  else:
    answer += 0

print(answer+N)