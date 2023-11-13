dial = {'ABC':3,'DEF':4,'GHI':5,'JKL':6,'MNO':7,'PQRS':8,'TUV':9,'WXYZ':10}
N = input()
answer = 0

for i in range(len(N)):   # N의 길이만큼 반복
  for j in dial.keys():   # dial의 키값을 돌림
    if N[i] in j:         # 문자가 딕셔너리의 키값에 속하면
      answer +=  dial[j]  # 키의 value값을 더해줌
    
print(answer)