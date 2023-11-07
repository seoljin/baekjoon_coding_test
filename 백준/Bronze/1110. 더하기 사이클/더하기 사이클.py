N = input() # 스트링으로 입력받기
n = int(N)  # int형으로도 하나 받아주기
cnt = 0
a = 0

while True: # break 나올 때까지 반복
  cnt += 1 
  if len(N) == 1: # N이 10 이하일 때
    N = str(0)+N  # 0N 형태로 나타내기
  a = int(N[-1]+str(int(N[0])+int(N[-1]))[-1])  # 문제에서 제시한 사이클
  if a == n:      # 사이클 돌린 결과와 입력받은 값이 같을 때 break
    break
  N = str(a)      # N에 다시 사이클 돌린 결과 받아서 반복

print(cnt)