N = int(input())

while N>0:  # N이 0보다 클 동안 반복
  answer = input()
  result = 0
  score = 0
  for i in answer:
    if i == 'O':      # 문자열 한글자씩 O일 때
      score += 1      # 1씩 증가
      result += score # 해당 값들을 result 변수에 저장 → 안그러면 X일때는 score가 0으로 초기화됨 
    else:
      score = 0
  N -= 1
  print(result)