A,B,C = map(int, input().split()) # 요금 입력받기
arr = [0]*100                     # 배열 입력받기
answer = 0

for i in range(3):                  # 3번 반복
  n, m = map(int, input().split())  
  for j in range(n,m):
    arr[j] += 1                     # arr에 입력받은 구간만큼 1을 더해줌, 중복되는 곳 표시가능
    
for k in arr:       # arr를 돌면서
  if k == 1:
    answer += A     # 1일때는 A만 더함
  if k == 2:
    answer += B*2   # 2일 때는 B*2를 더함
  if k == 3:
    answer += C*3   # 3일 때는 C*3을 더함
    
print(answer)