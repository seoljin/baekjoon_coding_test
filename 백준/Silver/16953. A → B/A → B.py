A, B = map(int, input().split()) # 입력받기
#print(B) # 확인용

answer = 1 # 연산 횟수/ 1에서 시작해야 출력할 때 오류나지않음/ answer+1 출력하다가 오류남

while True:
  if A > B:
    answer = -1 # A가 B보다 큰 경우에는 연산할 수 없음
    break
  elif A == B: # 같아졌을 때에는 while문을 빠져나가야한다.
    break
  elif B % 2 == 0:
    B = B//2
    answer += 1
  elif B % 10 == 1:  
    B = B//10
    answer += 1
  else:  # 이외의 경우(연산 후 A랑 B가 같지않은 경우)에는 -1 출력
    answer = -1
    break

print(answer)