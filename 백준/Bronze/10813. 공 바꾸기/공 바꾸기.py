N, M = map(int, input().split())
arr = [i for i in range(1,N+1)] # 1부터 N까지기때문에 1, N+1 로 범위 설정
num = 0

for i in range(M):
  i, j = map(int,input().split())
  num = arr[i-1]                    # 배열 값을 num에 저장 
  arr[i-1] = arr[j-1]               # 배열 j-1값을 i-1값에 넣음
  arr[j-1] = num                    # 저장해놨던 값을 arr[j-1]에 넣음
    
for i in range(N):
  print(arr[i], end=' ')