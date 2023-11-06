N = int(input())
arr = [[0]*100 for _ in range(100)] # 리스트 선언
answer = 0

for i in range(N):
  a, b = map(int, input().split()) # 위치 입력받기
  for j in range(10):              # 길이 10인 정사각형 → 10번 반복
    for k in range(10):
      arr[a+j][b+k] = 1            # 10번 움직이면서 1 입력하기
    
for i in range(100):
  for j in range(100):
    answer += arr[i][j]   # 100 번 돌리면서 값더하기
    
print(answer)